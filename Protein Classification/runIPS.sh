#!/usr/bin/env bash
#runIPS.sh

PATH="/usr/local/programs/jdk-11.0.9/bin/:$PATH"
export PATH

function scan {
           interproscan.sh -i proteins.fasta --iprlookup --goterms --pathways -f tsv -o proteins.tsv -cpu 4 -dp
}

scan 1>scan.log 2>scan.err
