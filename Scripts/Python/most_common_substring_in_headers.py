# the packages that we will need

import os # to navtigate the file system

from difflib import SequenceMatcher # to compare two strings

import argparse # this will help create CLI elements

# the way to access the commandline arguments is to use args.name_of_argument

# this is the name of the parser object that will parse the commandline
parser = argparse.ArgumentParser(description="This program will take in a the path to a folder, that should contain fasta files. It will then take in the files and then parse the headers to find the most common substring in the header.")

# the arguments will be coded in the following format
# parser.add_argument('--insert_name_here',nargs='?', const='bar',default=False, help='')

# provide the path to the folder that contains the fasta files
parser.add_argument('--loc',nargs='?', const='bar',default=False, help= "This should be the path(UNIX) path to the folder that holds the fasta files.")

# this should be the name of the new file
parser.add_argument('--out',nargs='?', const='bar',default=False, help='This should be the name of the will hold the output of the script')

# specify the extension of the files that you want to parse
parser.add_argument('--ext',nargs='?', const='bar',default=False, help='Use this to tell the program what the extension of the files should be.')

# do you want to pickle the output?
parser.add_argument('--Oform',nargs='?', const='bar',default=False, help='Use this to tell the program whether or not to pickle the output. The default will be to not pickle the output.')

# unsure about the function of this one
args = parser.parse_args()

curr = os.listdir(args.loc) # this variable will have the list of the names of the files in the folder

# change location to the folder with the fasta files
os.chdir(args.loc)

exten = f'.{args.ext}' # this is the extension of the files that you want to parse

dict_of_headers = {} # this is the dictionary that will hold the headers and their counts

for i in curr: # this is the name of the most recent fast file as received from line 32 or what has the name curr = os.listdir(args.loc)
    if i.endswith(exten):
        with open(i,'rt') as current_fasta_file:
            fasta_lines = current_fasta_file.readlines()
            
        list_namer = i.replace(".fa",'')
        list_namer = f'{list_namer}{"_list"}'
        list_namer= list()
        
        for file_lines in fasta_lines[:10]:
            if file_lines.startswith(">"):
                list_namer.append(file_lines)

        substring_counts={}

        for k in range(0, len(list_namer)):
            for j in range(k+1, len(list_namer)):
                string1 = list_namer[k]
                string2 = list_namer[j]
                match = SequenceMatcher(None, string1,string2).find_longest_match(0, len(string1), 0, len(string2))
                matching_substring=string1[match.a:match.a+match.size]
                if(matching_substring not in substring_counts):
                    substring_counts[matching_substring]=1
                else:
                    substring_counts[matching_substring]+=1

        # now we just write the final data to a dictionary
        try:
            dict_of_headers[i] = max(substring_counts, key=substring_counts.get).replace('\n','')
        except:
            print(i,"did not have proper data, so it could not be returned.")

if args.Oform == 'pickle':
    import pickle
    output_name = f'{args.out}.pickle'
    with open(output_name,'wb') as output_file:
        pickle.dump(dict_of_headers,output_file)