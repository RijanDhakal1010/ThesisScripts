import argparse # this will help create CLI elements

import pickle

import os

# this is the name of the parser object that will parse the commandline
parser = argparse.ArgumentParser(description=" This script takes an orthogroup with peptide sequences and generates a corresponding orthogroup with cds sequences. Two things are absoultely necessary, first a dict to identify the species in the sequence header using the most common subscript and dictified cds fastas with similar headers.")

# the arguments will be coded in the following format
# parser.add_argument('--insert_name_here',nargs='?', const='bar',default=False, help='') - If the default flag is false then there is no default.

parser.add_argument('--pickle',nargs='?', const='bar',default='Default', help= "This should be the location of the the pickled file with the species identification codes.")

# TODO : see if you can use * instead of extensions

parser.add_argument('--cds',nargs='?', const='bar',default=False, help='This should be the location of the cds fasta dicts in pickle format.')

parser.add_argument('--orthos',nargs='?', const='bar',default=False, help='The location of the orthos in Unix format.')

parser.add_argument('--output',nargs='?', const='bar',default=False, help='The location of the output files. Location should be in Unix format.')

# unsure about the function of this one
args = parser.parse_args()

try:
    with open(args.pickle,'rb') as species:
        species_codes = pickle.load(species)
except:
    print("Please make sure you supplied the correct location for the pickle")

def write_to_file(file_name,the_dict):

    file_name = file_name.split('.')[0]
    cds_base = f'{args.output}/{file_name}.cds'

    for l in the_dict:    
        line = l +  the_dict[l] + '\n'
        with open(cds_base,'a') as cds_handle:  
            cds_handle.write(line)

def list_to_cds_sequences(file_name,file_names_list):

    cds_headers = file_name

    cds_headers = {}
    
    for pep_header in file_names_list:
        for code_name in species_codes:
            if code_name in pep_header:
                species_name = species_codes.get(code_name)
        
                species_pickle = f'{args.cds}/{species_name}.pickle'

                try:    
                    with open(species_pickle,'rb') as cds_handle:   
                        cds_pickle = pickle.load(cds_handle)
                    sequence_cds = cds_pickle.get(pep_header.rstrip(),"None") # what are in peps may not be in cds. So, if it is in pep but not in cds then we do not want to send NoneType to the dict 
                    cds_headers[pep_header] = sequence_cds    
                except: 
                    print("Are you sure that ",species_pickle," exists?")

    write_to_file(file_name,cds_headers)    

def get_headers(file_name):
    file_name_loc = f'{args.orthos}/{file_name}'
    with open(file_name_loc,'r') as current_ortho_pep:
        current_ortho_pep_headers = current_ortho_pep.readlines()

    file_names_list = file_name
    file_names_list = []
    
    for pep_header in current_ortho_pep_headers:    
            if pep_header.startswith('>'):
                file_names_list.append(pep_header)
    
    list_to_cds_sequences(file_name,file_names_list)

def main():
    
    for ortho_pep in os.listdir(args.orthos):
        get_headers(ortho_pep)

main()