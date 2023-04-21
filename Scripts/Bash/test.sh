#!/bin/bash
list=$(ls -rS long_enough/*)
for file in $list
do
	base_name="$(basename $file .fa)"
	new_ext=".afa"
	new_file="$base_name$new_ext"
	echo $new_file
done
