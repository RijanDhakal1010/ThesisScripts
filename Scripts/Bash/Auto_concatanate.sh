#!/bin/bash
mkdir -p ~/Desktop/dump # this creates a directory at ~/Desktop/dump if it does not already exist
for folder in * # The way this script works is to have data in this structure parent_directory/species_folder/{bunch of unconnected files}. And we want to concatanate the unconnected files, in ~/Desktop/dump. To this end we create a for loop that accesses all the folders (i.e species_folders). Please make sure the folders underneath the parent directory are named for their species or at least what the final files should be. 
do # now we go into each species folder
    for file in $folder/* # now for each species folder we access all the aforementioned 'bunch of files'
    do # we do not want to mixup input and output
        test_name="${folder}.cat" # so here we use this method to replace the extension of the input files with .cat
        cat $file/* >> ~/Desktop/dump/$test_name # this appends the files to the name we created in the previous line 
    done # exit nested loop
done # exit parent loop
echo "All the concatanated files are now in a desktop folder named dump and have the extension .cat" # provide confirmation that the task is done.