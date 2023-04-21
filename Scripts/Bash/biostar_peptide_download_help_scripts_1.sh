#!/bin/bash
cat species.txt | while read SPECIES
do
	esearch -db protein -query "${SPECIES} [orgn]" | esummary | xtract -pattern DocumentSummary -element AssemblyAccession
done