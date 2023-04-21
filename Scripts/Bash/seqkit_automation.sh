#!/bin/bash 

# this is the shebang that the script will need to find bash.

for file in *.fa
do
	base_name="$(basename $file .fa)" # this removes the extension of the file
	new_ext=".afa"
	new_file="$base_name$new_ext"
	echo $out_file
	seqkit rmdup -s < $file > $new_file
done
