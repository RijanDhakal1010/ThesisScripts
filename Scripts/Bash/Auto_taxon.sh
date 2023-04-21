#!/bin/bash
IFS=$'\n'
list=$1
lines=$(cat $list)
n=1
for line in $lines
do
	echo "$n.$line"
	esearch -db taxonomy -query "$line" | efetch -format native -mode xml | xtract -pattern Taxon -block "*/Taxon" -unless Rank -equals "no rank" -tab "\n" -element Rank,ScientificName
	echo -e "End of $line\n"
	((n=n+1))
done < $list
