#!/usr/bin/env bash
#runQuast.sh

mkdir -p quast_output

quast.py -o ./quast_output \
    -s ./Rhodo/scaffolds.fasta \
    -t 4 \
    -R /data/METHODS/Fall/Module10/GCF_000012905.2_ASM1290v2_genomic.fna \
    -f \
    1>runQuast.log 2>runQuast.err
