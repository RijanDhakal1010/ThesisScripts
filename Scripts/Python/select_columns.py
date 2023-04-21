# to do :
 # 1. do not go forward if args are missing

import pandas as pd

import argparse # this is the library that will help us make use of commandline arguments

# this is the name of the parser object that will parse the commandline

parser = argparse.ArgumentParser(description="A script to make a subset of a dataframe based on columns. Provide a file with X number of columns, supply names of less than X columns names and create a new file with only coulmns of interest.")

# the arguments will be coded in the following format
# parser.add_argument('--',nargs='?', const='bar',default=False, help='')

# this is the argument that concerns the name of the file that will have the list of the names of columns to be kept
parser.add_argument('--name_list',nargs='?', const='bar',default=False, help= "This is the name of the list that has the columns that should stay in the new file.")

# This should be the full location of the old file
parser.add_argument('--old_file',nargs='?', const='bar',default=False, help=' This should be the full location of the old file.')

# The should be the name of the new file
parser.add_argument('--new_file',nargs='?', const='bar',default=False, help='Please supply the name of the new file.')

# unsure about the function of this one
args = parser.parse_args()

# make a list to supply to pandas
the_columns = ['desc','Orthogroup']

def main():

    # open the old file
    old_dataframe = pd.read_csv(args.old_file,sep='\t')

    # open file with list of names
    with open(args.name_list) as file:
        column_names = file.readlines()

    for i in column_names:
        i = i.rstrip()
        the_columns.append(i)
    
    print(the_columns)

    new_dataframe = old_dataframe.filter(the_columns)

    new_dataframe.to_csv(args.new_file, index=False,sep="\t")


main()
