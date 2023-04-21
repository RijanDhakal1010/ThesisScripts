# the purpose of this script is to synchronize the headers and the sequences of onekp dataset.

import os
import pandas as pd
import argparse

Help_text = "The purpose of the this script is to synchronize the headers and the sequences of onekp dataset. Please take note of the flags to supply the proper input."

parser = argparse.ArgumentParser(description=Help_text) # This is not the typical way of adding help_text. Just personal prefrance.

# create argument groups
action_group = parser.add_argument_group('Action arguments')
location_group = parser.add_argument_group('Location arguments')

location_group.add_argument('--pep',nargs='?',help="The location of the peptide files.")

location_group.add_argument('--cds',nargs='?',help="The location of the cds files.")

location_group.add_argument('--sync',nargs='?',help="The location of the synced files.")

location_group.add_argument('--miss',nargs='?',help="The location of the files showing missing sequences.")

action_group.add_argument('--pepext',nargs='?', const='.faa', default="faa",help=" The extension of the peptide files. If not supplied,'faa' will be used.")

action_group.add_argument('--nucext',nargs='?',default="cds",help="The extension of the cds files. If not supplied,'cds' will be used.")

args = parser.parse_args()

def main():
    # this make sure that the supplied locatiion actually exist
    for action in parser._action_groups:  # Loop through argument groups
        if action.title == 'Location arguments':  # Find the location group
            for argument in action._group_actions:  # Loop through location arguments
                arg_value = getattr(args, argument.dest)
                if os.path.exists(arg_value):
                    pass
                else:
                    print(f"Cannot open '{arg_value}', please make sure it exits or the path is supplied correctly.")


    filelist = [i.rsplit('.')[0] for i in os.listdir(args.pep)]

    pep_counts = {}

    for i in filelist:
        file = f"{args.pep}/{i}.{args.pepext}"
        with open(file, "r") as in_file:
            pep_counts[i] = sum(line.count(">") for line in in_file)

    nuc_counts = {}

    for i in filelist:
        file = f"{args.cds}/{i}.{args.nucext}"
        with open(file, "r") as in_file:
            nuc_counts[i] = sum(line.count(">") for line in in_file)
         
    missing_count = {}

    for i in filelist:
        pep_headers = []
        nuc_headers = []
        count = 0

        with open(f"{args.pep}/{i}.{args.pepext}",'r') as pep_file:
            pep_file_lines = pep_file.readlines()
    
        with open(f"{args.cds}/{i}.{args.nucext}",'r') as nuc_file:
            nuc_file_lines = nuc_file.readlines()

        for j in pep_file_lines:
            if j.startswith('>'):
                pep_headers.append(j.strip())
    
        for k in nuc_file_lines:
            if k.startswith('>'):
                nuc_headers.append(k.strip())
    
        with open(f"{args.miss}/{i}.missing","w") as missing_file:
            for l in pep_headers:
                if l not in nuc_headers:
                    count = count + 1
                    lline = l + '\n'
                    missing_file.writelines(lline)
    
        missing_count[i] = count

    df = pd.DataFrame(list(missing_count.items()), columns=['Code','count'])

    df.sort_values(by='count',ascending=False).to_csv("Missing_counts_log.tsv", sep='\t',index=False)

    for i in filelist:
        pep_headers = [] # using list because lists can have duplicates but dicts cannot (by default)
        pep_fasta = {} # this helps work with the header and sequence structure of Fastas.
        nuc_headers = []
        count = 0

        with open(f"{args.pep}/{i}.{args.pepext}",'r') as pep_file:
            pep_file_lines = pep_file.readlines()
    
        with open(f"{args.cds}/{i}.{args.nucext}",'r') as nuc_file:
            nuc_file_lines = nuc_file.readlines()
    
        for k in nuc_file_lines:
            if k.startswith('>'):
                nuc_headers.append(k.strip())

        for index, header in enumerate(pep_file_lines):
            if header.startswith('>'):
                pep_headers.append(header.rstrip())
                sequence = pep_file_lines[index + 1]
                pep_fasta[header.rstrip()] = sequence 
    
        with open(f"{args.sync}/{i}.syncup","a") as syncup:
            for l in pep_headers:
                if l in nuc_headers:
                    line = l + '\n' + pep_fasta[l]
                    syncup.writelines(line)
                else:
                    continue

main()
