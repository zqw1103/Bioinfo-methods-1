#!/usr/bin/env python3
# interleave.py

from Bio import SeqIO

leftReads = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq", "fastq")
rightReads = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R2.fastq", "fastq")

totalreads = []
for left, right in zip(leftReads, rightReads):
    totalreads.append(left)
    totalreads.append(right)

with open('Interleaved.fasta', 'w') as out:
    SeqIO.write(totalreads, out, 'fasta')
