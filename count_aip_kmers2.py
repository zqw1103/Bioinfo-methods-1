#!/usr/bin/env python
#count_aip_kmers.py

import re
import os

filename = '/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq'

kmer_dict = {}
kmer_len = 6

with open(filename, 'r') as file:
    for line in file:
        line = ''.join(line.split('\n'))
        if re.match('[ATCGN]+$', line):
            stop = len(line) - kmer_len + 1
            for start in range(0, stop):
                kmer = line[start : start + kmer_len]
                if kmer in kmer_dict:
                    kmer_dict[kmer] += 1
                else:
                    kmer_dict[kmer] = 1

def wirte_tab_count(kmer_dict):
    with open('/home/wang.zunq/BINF6308/module-03-zqwang1103/aip_kmers2.txt', 'w') as out:
        for k, v in kmer_dict.items():
            out.write("{0}\t{1}\n".format(k,v))
    out.close()

wirte_tab_count(kmer_dict)
