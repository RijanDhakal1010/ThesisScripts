#!/bin/bash

source /opt/asn/etc/asn-bash-profiles-special/modules.sh
module load mafft/7.481_gcc9

for file in *.fa
do
	base_name="$(basename $file .fa)"
	new_ext=".aafa"
	new_file="$base_name$new_ext"
	mafft --auto $file > $new_file
done
