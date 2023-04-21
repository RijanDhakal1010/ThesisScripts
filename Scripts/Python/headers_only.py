import argparse # this will help create CLI elements

import os # Needed for filepath navigation

# this is the name of the parser object that will parse the commandline
parser = argparse.ArgumentParser(description="Use this to get the headers of the orthofiles.")

# the arguments will be coded in the following format. If the default flag is false then there is no default.
# parser.add_argument('--insert_name_here',nargs='?', const='bar',default=False, help='') 


parser.add_argument('--inloc',nargs='?', const='bar',default=".", help=' This should be the location of the input files and the path should be in Unxi format. If no input is provided then the current directory will be used')

parser.add_argument('--outloc',nargs='?', const='bar',default='Headers', help= "This should be the location of the output files in Unix format. If you no location is provided a directory in the same folder named 'Headers' will be used")

# unsure about the function of this one
args = parser.parse_args()

def writer(fasta_list,name):
	
	with open(name,'a') as w:
		w.writelines(fasta_list)

def main():

    if (os.path.exists(args.outloc)) == False:
        os.makedirs(args.outloc)

    if (os.path.exists(args.inloc)) == False:
        print("Are you sure your directory of input files exists?")
    else:
        os.chdir(args.inloc)

    for i in os.listdir():

        infile_name = i.split('.')[0]
        print(infile_name)
        outfile_name = f'{args.outloc}/{infile_name}.hfa'
        infile_name = list()
        

        if i.endswith('.fa'):
            with open(i,'r') as current_input_file:
                current_file_lines = current_input_file.readlines()

            for j in current_file_lines:
                if j.startswith('>'):
                    infile_name.append(j)
                
            writer(infile_name,outfile_name)

main()
