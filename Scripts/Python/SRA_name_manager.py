# When you download a file from SRA, it will not always have the exact header that you want it to. This script is there to help with this very specific problem.

import re # this library is to deal with regular expressions

import sys # this library is to deal with sys arguments

import os # this is the library for parsing the file tree

from difflib import SequenceMatcher

# list of flags

# -l flag will be used for the file location

def most_common_string(the_file): # the function that will detect and return the most common string in the headers, so that they can be replaced.

	with open(the_file,'rt') as current_fasta_file:
		fasta_lines = current_fasta_file.readlines()

	list_namer = the_file.replace(".fasta",'')
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

	try:
		return(max(substring_counts, key = substring_counts.get))
	except:
		print(the_file,"Did not have proper data, so it could not be returned.")			


def fasta_runner(list_of_fastas): # this is the function where the files will be opened and written

	for i in list_of_fastas: # this gets the list of the names of fasta files if there are any.
		common_string = most_common_string(i) # this is where we will send the file name to another function that will find the most common string for us. That is, the most common string in the headers throughout the fasta file.
		no_ex = i.replace(".fasta","") # this removes the extension, which will make it easy for us to work with the name
		no_ex = f'{">"}{no_ex}' # this is to make the new headers that have the > sign in from of them

		nu = f'{i}{".header_changed"}' # this to to make the new file that will be a copy of the old files except for the new headers

		with open(i,'rt') as file_to_write: # this reads the files lines
			lines_to_replace = file_to_write.readlines()

		new_headers = ""

		for the_headers in lines_to_replace: # for each file line
			if the_headers.startswith(">"):
				new_headers = the_headers.replace(" ","_")
				new_headers = new_headers.replace(common_string,no_ex)
			else:
				new_headers = the_headers 

			writing_file = open(nu,"a")
			writing_file.write(new_headers)
			writing_file.close()

def fastas_in_the_folder(location): # this is the function that will generate the list of fasta files

	os.chdir(location)

	list_of_fastas = list()

	for root_path, dir_names, files_names in os.walk(location,topdown = True):
		for file_name in files_names:
			if file_name.endswith(".fasta"): # this has the added benefit of not working on the same file multiple times over.
				list_of_fastas.append(file_name)

	if len(list_of_fastas) != 0: # this is to make sure that script does not crach if the folder does not have any fastas at all
		fasta_runner(list_of_fastas) # this is the function that will open the fasta files and make replacements in the headers

	else:
		print("This folder does not have any fastas.")


	return 0

def params(): # this is the function where the majority of the action will take place

	list_of_arguments = list() # creating a list to receive the sys arguments

	list_of_arguments = sys.argv[1:] # this is the way to ignore the first sys arg, since it will just be "python"

	try:
		location = list_of_arguments[list_of_arguments.index("-l") + 1]
	except:
		print("Note: You did not provide a custom location with the -l flag, so the program will take the current location as the address of exceution.\n")
		location = os.getcwd()

	# try:
	# 	preferred_header = list_of_arguments[list_of_arguments.index("-p") + 1]
	# except:
	# 	print("Note:You did not provide a custom header for the task, hence the file's name with spaces removed will be used for the operation.")

	fastas_in_the_folder(location) # this will call the named function, the function does not return anything here

params()