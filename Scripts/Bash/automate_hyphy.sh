#!/bin/bash 

for file in *.pal
do
	base_name="$(basename $file .pal)"
	new_ext=".pal.treefile"
	treefile="$base_name$new_ext"
	echo `(echo "1"; echo "6"; echo $file; echo $treefile) | hyphy`
done
