#!/usr/bin/env python3
# find_dmel_orf.py

import re
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

file = '/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta'
for record in SeqIO.parse(file, 'fasta'):
    if re.match('^\d{1}\D*$', record.id):
        dna = record.seq
        rna = dna.transcribe()
        orf = re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)',str(rna)).group()
        protein = Seq(orf).translate()
        print(protein)
        
