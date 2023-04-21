import argparse # this will help create CLI elements

import os

# this is the name of the parser object that will parse the commandline
parser = argparse.ArgumentParser(description="This script should take cds files in one folder (with 'None' coded traanscripts), a second folder with peptide files that have no 'None' and a third folder where an output file is produced that only has the intersection of headers between the cds file from the first folder and the headers of the peptide files in the second folder. and remove all the headers with 'None' transcripts in each file.")

# the arguments will be coded in the following format
# If the default flag is false then there is no default.
# nargs is the number of argument
# The first argument is the flag name
# parser.add_argument('--',nargs='?', const='bar',default=False, help='') 

parser.add_argument('--peps',nargs='?', const='bar',default='Default', help= "This is the path to the directory where the old peptide files with the superset of headers are. Make sure not to give a trailing slash at the end, python adds that on its own.")

parser.add_argument('--cds',nargs='?', const='bar',default=False, help='This is path to the folders with the None coded cds files are. Make sure not to supply the trailing slash at the end, python does that on its own.')

parser.add_argument('--pepext',nargs='?', const='bar',default=".pep", help='The extension of the cds peptide files. Please supply one or .fa will be used by default. And if you do supply one do not forget the dot.')

parser.add_argument('--CDSext',nargs='?', const='bar',default=".cds", help='The extension of the cds peptide files. Please supply one or .fa will be used by default. And if you do supply one do not forget the dot.')

parser.add_argument('--out',nargs='?', const='bar',default=False, help='This is the location where the output files will be delivered. Make sure not to supply the trailing slash at the end, python does that on its own.') 

# unsure about the function of this one
args = parser.parse_args()


def run():

    for i in os.listdir(args.cds):

        nuc_dict = {}

        pep_dict = {}

        l = i.rsplit('.')[0] # this takes the files and retains only their basename in l

        k = f'{args.out}{l}{".no_nones"}{args.pepext}' # this is to make the output file later
        
        l = f'{args.peps}{l}{args.pepext}' # this is to acces the pepfile

        j = f'{args.cds}{i}' # this one does not need the {args.CDSext} because it can access the files through the for loop. 

        with open(j,'r') as nucleo:
            nucleo_lines = nucleo.readlines()
        
        with open(l,'r') as peptides:
            peptide_lines = peptides.readlines()

    
        for index,header in enumerate(nucleo_lines):
            if header.startswith('>'):
                sequence = nucleo_lines[index + 1]
                if sequence.rstrip() != "None":
                    nuc_dict[header] = sequence
        
        for index1,header1 in enumerate(peptide_lines):
            if header1.startswith('>'):
                sequence1 = peptide_lines[index1 + 1]
                pep_dict[header1] = sequence1
        
        for header3 in nuc_dict:
            line = header3 + pep_dict.get(header3)
            with open(k,'a') as writer:
                writer.write(line)



def main():

    if os.path.isdir(args.peps) == False:
        print("Cannot access ", args.peps,", are you sure it is there? Please make note of the extensions in the CLI")
        quit()
    
    if os.path.isdir(args.out) == False:
        print("Cannot access ", args.out,", are you sure it is there?")
        quit()

    if os.path.isdir(args.cds) == False:
        print("Cannot access ", args.cds,", are you sure it is there?")
        quit()
    
    run()
    

main()