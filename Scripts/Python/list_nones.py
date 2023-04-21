import os

def main():

    for files in os.listdir():
        file = files.split('.')[0]

        new_file = f'{file}.none'

        with open(files,'r') as current_files:
            current_file_lines = current_files.readlines()
        
        file = {}

        for index,header in enumerate(current_file_lines):
            if header.startswith('>'):
                sequence = current_file_lines[index + 1]
                if sequence.rstrip() == 'None':
                    file[header] = sequence
        for header in file:
            with open(new_file,'a') as writer:
                writer.write(header)

main()
