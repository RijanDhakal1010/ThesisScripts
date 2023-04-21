#!/bin/bash

while [[ "$#" -gt 0 ]]; do
    case $1 in
        -t|--target) target="$2"; shift ;;
	#to add new arguments use the following line as format
	    -e|--ext) ext="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

for file in $target*.$ext
do
    base_name="$(basename $file .$ext)"
    new_ext=".*"
    wildcard="$target$base_name$new_ext"
    rm $wildcard
done
