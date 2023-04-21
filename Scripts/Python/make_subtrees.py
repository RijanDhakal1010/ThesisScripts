import pandas as pd # this will help wrangle the data

import argparse # this will help create CLI elements

# this is the name of the parser object that will parse the commandline
parser = argparse.ArgumentParser(description=" This script is desigened to take a csv file with taxonomic information. The input file should be a two dimensinal csv files, where the first column should be the names of species and all other columns should have the taxonomic data for the respective species. One level per column. ")

# the arguments will be coded in the following format
# parser.add_argument('--insert_name_here',nargs='?', const='bar',default=False, help='')

parser.add_argument('--input',nargs='?', const='bar',default=False, help= "The path to the input csv file. This should be in UNIX format.")

parser.add_argument('--list',nargs='?', const='bar',default=False, help='The path to the file that has the list of names that you want to filter into the output file.')

parser.add_argument('--output',nargs='?', const='bar',default=False, help='The name of the output file, you can supply a path to where you want the file to go. If you do provide a path, make sure it is in the UNIX format.')

# unsure about the function of this one
args = parser.parse_args()

def main():

	dataframe = pd.read_csv(args.input)

	with open(args.list,'r') as list_file:
		list_lines = list_file.readlines()

	name_list=[]

	for i in list_lines:
		i = i.rstrip()
		name_list.append(i)

	mask = dataframe.applymap(lambda s: not set(s.split(',')).isdisjoint(name_list)).any(1) # here mask is the boolean matrix that has the same length as the dataframe. The mask is true if the row contains one of the names in the list.

	newframe = dataframe[mask] # apply the boolean mask to the dataframe

	# this code currently does not check if there already exists a file with the same name. This could casue issues, since that could append where it should not append but I will resovle that later.

	# I have chosen not to use `with open` since using one open and one close seems a little simpler in this situation. At least to me, at this point in time.

	filewriter = open(args.output,"a")

	for i in newframe.iloc[:,0]:
		i = i + '\n'
		filewriter.write(i)

	filewriter.close()
	
main()