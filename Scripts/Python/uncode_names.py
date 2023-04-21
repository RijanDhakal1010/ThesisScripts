import argparse # this will help create CLI elements
import pickle
import shutil
import os

# this is the name of the parser object that will parse the commandline
parser = argparse.ArgumentParser(description="This script takes a dict, a folder and then renames the files in the folder from from the dict's keys to the keys' respective values (so long as the file names and the keys match).")

# the arguments will be coded in the following format
# If the default flag is false then there is no default.
# nargs is the number of argument
# The first argument is the flag name
# parser.add_argument('--',nargs='?', const='bar',default=False, help='') 

parser.add_argument('--pickle',nargs='?', const='bar',default='Default', help= "This should be the location of the pickled dict. The dict should have the codes as the keys and the full names as the values.")

parser.add_argument('--old', nargs='?', const="bar", default=False, help ="Location of the old files with the codes as the file names. Provide the name in unix format and make sure it is the full path.")

parser.add_argument('--new', nargs='?', const="bar", default=False, help="This should be the location of the new folder where the new renamed files will de pasted. Provide full path in unix format.")

parser.add_argument('--ext', nargs='?', const="bar", default='fa', help="Extension of the files you are interested in. If not supplied manually 'fa' is used by default.")

# unsure about the function of this one
args = parser.parse_args()

def main():

    try:
        with open(args.pickle,'rb') as codes:
            code_names = pickle.load(codes)
    except:
        print("Is the pickle file properly named or accessible? Python cannot open it.")
    
    filename_list = []
    for filename in os.listdir(args.old):
        filename_list.append((filename.split('.')[0]))
    
    n=0
    for key in code_names:
        if key in filename_list:
            origin = f'{args.old}/{key}.{args.ext}'
            destination = f'{args.new}/{code_names[key]}.{args.ext}'
        if os.path.isfile(destination):
            n += 1
            destination = f'{args.new}/{code_names[key]}_{n}.{args.ext}'
            shutil.copy(origin, destination)
        else:
            shutil.copy(origin, destination)
                        
main()
