import os

def main():

    for files in os.listdir():
        file = files.split('.')[0]

        new_file = f'{file}.clean.fna'

        with open(files,'r') as current_files:
            current_file_lines = current_files.readlines()
        
        file = {}

        for index,header in enumerate(current_file_lines):
            if header.startswith('>'):
                sequence = current_file_lines[index + 1]
                if sequence.rstrip() != 'None':
                    file[header] = sequence
                else:
                    continue

        for header in file:
            line = header + file[header]
            with open(new_file,'a') as writer:
                writer.write(line)

main()
