# first define a variable that will be reused often
codon_dict = {
   'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
   'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
   'ATT':'I','ATC':'I','ATA':'I','ATG':'M',
   'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
   'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
   'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
   'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
   'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
   'TAT':'Y','TAC':'Y','TAA':'*','TAG':'*',
   'CAT':'H','CAC':'H','CAA':'Q','CAG':'Q',
   'AAT':'N','AAC':'N','AAA':'K','AAG':'K',
   'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
   'TGT':'C','TGC':'C','TGA':'*','TGG':'W',
   'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
   'AGT':'S','AGC':'S','AGA':'R','AGG':'R',
   'GGT':'G','GGC':'G','GGA':'G','GGG':'G'
}

# then define helpful functions
def get_rev_comp(seq):

    base_pairs = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

    rc = ''

    for b in seq:
        rc += base_pairs[b]

    return rc[::-1]

def get_codons(seq):

    polypeptide = ''

    for start in range(0,len(seq)-2,3):
        end = start + 3
        polypeptide += codon_dict[seq[start:end]]

    return polypeptide

# now define the variables we need and make the various function calls
seq = 'GCCTGACTTCGACCTGATCA'
AA_fwd = dict()
AA_rev = dict()

for frame in [0,1,2]:
    AA_fwd[frame] = get_codons(seq[frame:])
    AA_rev[frame] = get_codons(get_rev_comp(seq)[frame:])

print(AA_fwd)
print(AA_rev)