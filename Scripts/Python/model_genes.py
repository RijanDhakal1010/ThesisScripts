import pandas as pd

import argparse

from pathlib import Path
#Path("/my/directory").mkdir(parents=True, exist_ok=True)

from argparse import RawTextHelpFormatter

# this is the name of the parser object that will parse the commandline
parser = argparse.ArgumentParser(
    description='Purpose: grab homologs of specified species from the exhaustive matrix of homologs.\n This scirpt depends on getting the right kind of files as input.\n Reading the following options carefully to proceed.', formatter_class=RawTextHelpFormatter) # this will help create CLI elements

# the arguments will be coded in the following format
# If the default flag is false then there is no default.
# nargs is the number of argument
# The first argument is the flag name
# parser.add_argument('--',nargs='?', const='bar',default=False, help='') 

parser.add_argument('--tsv',nargs='?', const='bar',default='Default', help= "The file that contains all of the homologs. If your file has a different delimiter you will have to change that within the script.")

parser.add_argument('--specific_families',nargs='?', const='bar',default=False, help='A text file that contains one family name per line. The names should correspond to the names within the tsv file.')

parser.add_argument('--specific_speices',nargs='?', const='bar',default=False, help='A text file that contains one species name per line. The names should correspond to the names within the tsv file.') 

parser.add_argument('--format',nargs='?', const='bar',default=False, help='If you want the format as a table pass "table" and if you want files per family pass "separate"')

parser.add_argument('--outdir',nargs='?', const='bar',default="model_genes", help='The name of the directory that you want your data deposited in. Please supply a name otherwise "model_genes" will be used by default.') 

# unsure about the function of this one
args = parser.parse_args()

def text_output_manager(species_list,df):

    df = df.fillna('Empty_homolog')

    Path(args.outdir).mkdir(parents=True, exist_ok=True)
    by_family = f"{args.outdir}/By_family"
    Path(by_family).mkdir(parents=True, exist_ok=True)
    for i in species_list:
        name = f"{args.outdir}/{i}" # folder per list
        Path(name).mkdir(parents=True, exist_ok=True)
    
    for i in species_list:
        df1 = pd.DataFrame()
        df1['Family'] = df[df.columns[0]]
        df1['Genes'] = df[i]
        for j in df1.itertuples():
            ifile = f"{args.outdir}/{i}/{j[1]}.homolog"
            if type(j[2]) != float:
                lines = j[2].rsplit(',')
                line = str()
                for l in lines:
                    line = line + l.rstrip().lstrip() + '\n'
                #lines = j[2].replace(',','\n')
                with open(ifile,'a') as currentfile:
                    file_writer = currentfile.writelines(line)
            elif type(j[2]) == float:
                with open(ifile,'a') as currentfile:
                    file_writer = currentfile.write("No genes for this species in this homolog.")

    for i in df.itertuples():
        family_name = f"{by_family}/{i[1]}.homolog"
        with open(family_name,'a') as currentfile:
            for j,l in zip(i[2:],df.columns[1:]):
                lines = j.rsplit(',')
                line = str()
                for k in lines:
                    line = k.rstrip().lstrip() + '\n' + line
                finalline = f'Species Demarcation:{l.rstrip()}\n' + line
                #lines = f'Species Demarcation:{l.rstrip()}\n' + str(j.replace(',','\n')) + '\n'
                file_writer = currentfile.writelines(finalline)
            
    

def subset():

    family_list = list() # This list will be used to filter the rows of the larger dataset in pandas

    species_list = list() # This list will be used to filter the columns of the larger dataset in pandas

    df = pd.read_csv(args.tsv, sep = '\t',low_memory=False)

    with open(args.specific_families,'r') as family_list_reader:
        families = family_list_reader.readlines()

    with open(args.specific_speices,'r') as species_list_reader:
        species = species_list_reader.readlines()

    for i in species: 
        i = i.rstrip()
        if i not in species_list: # to avoid repeats
            species_list.append(i)
    
    for j in families:
        j = j.rstrip()
        if j not in family_list: # to avoid repeats
            family_list.append(j)

    # filter dataframe for specified rows and columns by name. rows first and columns second

    df = df[df[df.columns[0]].isin(family_list)] # filter rows against names of families

    family_names = df[df.columns[0]] # we will need family names in the script and better to just make it standard. This will only work if family names are the first column. Make sure this sits after the row based filteration.

    df = df.loc[:, df.columns.isin(species_list)] # filter datafrmae for specified list of species names. Species names are columns. According to SO df.loc[:, df.columns.isin(['nnn', 'mmm', 'yyy', 'zzzzzz'])]

    df.insert(loc=0, column='Families', value=family_names) # reinsert the family names

    if args.format == 'Table':
        df.to_csv('List of model genes in homologs.tsv',sep='\t',index=False)
    elif args.format == 'separate':
        text_output_manager(species_list, df)

def open_input():

    try:
        test_frame = pd.read_csv(args.tsv, sep='\t',low_memory=False)
    except:
        print('Are you sure you supplied the homolog file properly?')
        quit()
    
    try:
        with open(args.specific_families,'r') as family_list_reader:
            family_list = family_list_reader.readlines()
    except:
        print('Are you sure you supplied the family list file properly?')
        quit()
    
    try:
        with open(args.specific_speices,'r') as species_list_reader:
            species_list = species_list_reader.readlines()
    except:
        print('Are you sure you supplied the species list file properly?')
        quit()
    
    subset()

open_input()