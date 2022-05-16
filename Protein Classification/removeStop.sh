#!/usr/bin/env bash
#removeStop.sh

input=~/BINF6308/module-08-zqwang1103/BLAST/Trinity.fasta.transdecoder.pep
sed  's/\*//' $input | head  -n5000 > proteins.fasta
