#!/bin/bash
IFS=$'\n'
list=$1
lines=$(cat $list)
n=1
for line in $lines
do
	gdown $line
done < $list