#!/bin/bash

ulimit -n 13000

source /opt/asn/etc/asn-bash-profiles-special/modules.sh
module load orthofinder/2.5.2

orthofinder -f peptides -t 32
