#!/bin/bash
cat species.txt | while read SPECIES; do 
  datasets summary genome taxon "${SPECIES}" --reference |\
  jq -r '[.assemblies[].assembly 
  | .org.sci_name,.org.tax_id,.assembly_accession] 
  | @tsv'; 
done
