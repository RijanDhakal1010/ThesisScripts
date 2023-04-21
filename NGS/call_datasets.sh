#A dependency of this script is NCBI datasets 
#to install NCBI go to https://www.ncbi.nlm.nih.gov/datasets/docs/v2/download-and-install/
# supply the list of species as a file with one species name per line, this should be the first commandline arg

#!/bin/bash
IFS=$'\n'
list=$1
lines=$(cat $list)
n=1
for line in $lines
do
    filename="${line// /_}.json"
    datasets summary genome taxon $line --assembly-level complete > $filename
    ((n=n+1))
done < $list
