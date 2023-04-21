#!/bin/bash

while [[ "$#" -gt 0 ]]; do
    case $1 in
        -fd|--first_directory) first_directory="$2"; shift ;;
	#to add second arguments use the following line as format
	-sd|--second_directory) second_directory="$2"; shift ;;
	-td|--third_directory) third_directory="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

for file in $first_directory/*.pal.treefile
do
	base_name="$(basename $file .pal.treefile)"
	new_ext=".pal"
	first_pal_name="$second_directory$base_name$new_ext"
	second_pal_name="$third_directory$base_name$new_ext"
	cp $first_pal_name $second_pal_name
done
