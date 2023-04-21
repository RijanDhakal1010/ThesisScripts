#!/bin/bash

for file in *.fa
do
	base_name="$(basename $file .fa)"
	new_ext=".afa"
	new_file="$base_name$new_ext"
	awk '{if(NR==1) {print $0} else {if($0 ~ /^>/) {print "\n"$0} else {printf $0}}}' $file > $new_file
done
