#!/bin/bash

while [[ "$#" -gt 0 ]]; do
    case $1 in
        -t|--target) target="$2"; shift ;;
	#to add new arguments use the following line as format
	-d|--destination) destination="$2"; shift ;;
	-e|--ext) extension="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

homepath=$(pwd)

target="$homepath/$target"
destination="$homepath/$destination"


rsync -a --include '*/' --include "*.$extension" --exclude '*' "$target"/ "$destination"/

