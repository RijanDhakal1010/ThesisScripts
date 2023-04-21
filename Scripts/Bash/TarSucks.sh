#!/bin/bash
mkdir -p extracted
for file in *.tar.bz2
do
    filename="${file%.faa.tar.bz2*}"
    mkdir -p extracted/$filename
    tar -xvf $file -C extracted/$filename/
done
echo "Extracted all files are in a folder name extracted"