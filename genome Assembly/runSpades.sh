#!/usr/bin/env bash
#runSpades.sh

mkdir -p Rhodo
/usr/local/programs/SPAdes-3.14.1-Linux/bin/spades.py \
-1 Paired/SRR522244_1.fastq -2 Paired/SRR522244_2.fastq \
-t 4 \
-o Rhodo \
1>runSpades.log 2>runSpades.err
