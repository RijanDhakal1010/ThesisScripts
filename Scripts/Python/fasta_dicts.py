import pickle # this is the package needed to make pickles
import os # this is the package need to parse the file system
import argparse # this is the package needed to make the commandline arguments

# this is the name of the parser object that will parse the commandline
parser = argparse.ArgumentParser(description="This script will take a directory and convert all the fasta files in directory in pickled dicts, where the name of the sequence is the key and the sequence is the value. The fasta file extension that are read by defaul are .fna, .faa, .fa and .pep. The out files will always have pickle extensions.")

# the arguments will be coded in the following format
# parser.add_argument('--insert_name_here',nargs='?', const='bar',default=False, help='') - If the default flag is false then there is no default.

parser.add_argument('--loc',nargs='?', const='bar',default='.', help= "This is the flag to supply the location of the directory where you have the fasta file. Without the flag supplied the default location is going to be the current folder.")

parser.add_argument('--ext',nargs='*',default='Default', help="Supply the extension of the files that you want pickled else all files will be pickled.")

# unsure about the function of this one but best I can tell it gathers all the args into one object
args = parser.parse_args()

def main():

    if args.loc == '.':
        file_names = os.listdir('.')
    else:
        os.chdir(args.loc)
        file_names = os.listdir() # accessing the loc from within the loc gives an error. So, change this to the current location instead of the loc.

    file_list = []

    if args.ext != "Default":
        suffixes = tuple(args.ext)
        for i in file_names:
            if i.endswith(suffixes):
                file_list.append(i)
    else:
        for i in file_names:
                file_list.append(i)

    for i in file_list:

        i = str(i)

        file_name = i.split('.')[0]

        print(file_name)

        pickle_name = f'{file_name}.pickle'

        file_dict = dict()

        with open(i,'r') as current_file:
            current_sequences = current_file.readlines()
        
        for index,elem in enumerate(current_sequences):
            if elem.startswith('>'):
                elem = elem.rstrip()
                sequence = current_sequences[index+1]
                sequence = sequence.rstrip()
                file_dict[elem] = sequence

        with open(pickle_name,'wb') as handle:
            pickle.dump(file_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
        

main()
