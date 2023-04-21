import argparse # this will help create CLI elements

import pickle # this is what we will use to open the pickled dict.

# this is the name of the parser object that will parse the commandline
parser = argparse.ArgumentParser(description=" I am writing this specifically to replace the four letter codes of the OneKP official trees with species names. This code can be used to replace the old strings of a file with new strings guided by a dict where the old strings are keys and the new strings are values. ")

# the arguments will be coded in the following format
# parser.add_argument('--insert_name_here',nargs='?', const='bar',default=False, help='') - If the default flag is false then there is no default.

parser.add_argument('--file',nargs='?', const='bar',default=False, help= "This should be the unix-format path to the file that we want to work on.")

parser.add_argument('--dict',nargs='?', const='bar',default=False, help='This should be the unix-format path to the dict file. In the dict file the strings you want to replace must be the keys and the new strings you want to insert must be the keys. Please be careful of whitespaces and newline characters.')

parser.add_argument('--output',nargs='?', const='bar',default=False, help='This should be the name of the output file.')

# unsure about the function of this one
args = parser.parse_args()

def main():

    try:
        with open(args.file) as TheFile:
            TheFileLines = TheFile.readlines()
    except:
        print("Please make sure that the file is there and the path is in unix format.")

    try:
        with open(args.dict,'rb') as handle:
            our_dict = pickle.load(handle)
    except:
        print("Please make sure that the file is there and the path is in unix format.")
    
    file_output = open(args.output,'wt')
    
    for i in TheFileLines:
        for key in our_dict:
            i = i.replace(key,our_dict[key])
        file_output.write(i)

main()
