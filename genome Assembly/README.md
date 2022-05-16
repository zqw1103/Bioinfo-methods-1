Methods:
getNGS.sh:

-implement fast-dump to retrieve raw sequence reads by specifying option split-files on SRR522244
trim.sh:

-implement QC using trimmamotic with PE as pair-end, -threads 1 for threads set to 1, -phred33 based on quality scores in the format of phred33
HEADCROP 0 base to remove from beginning regardless quality
ILLUMINACLIP: :2:30:10 provides number of mismatches
LEADING:20 TRAILING:20 specify minimum quality at start and end of reads
SLIDINGWINDOW:4:30 indicates slide window and associated minimum quality
MINLEN:36 determine the length of reads to keep
runSpades.sh:

-run spades.py specifying 2 reads, -t threads with 4, -o output dir, store log in runSpades.log, store the errors in runSpades.err.
runQuast.sh:

-run quast.py by specifying -o output dir, -s split scaffolds by reference genome, -t 4 threads, -R for reference genome, -f option to complete gene finding, store log in runQuast.log, store the errors in runQuast.err.
Conclusions from Analysis:

Scaffolds_broken is formed by split of assemblies by continuous fragments of N's of length ≥ 10
total_length:{scaffolds=4531725;ref=4602977} so scaffolds is shorter than reference.
N50:{scaffolds=27657;scaffolds_broken=25496} so N50 of scaffolds is larger, which is expected.
number of genes:{ref=4468;predicted=4471} so more genes are predicted than reference.

Nx plot: It dispalys largest contig length L such that contigs more than L accounts for at least x% of bases of assembly. We can confirm by looking at N50 and compared to table result.

GC content: total G and C nts in the assembly divided total length, could be computed without reference genome. It is about 69% and can be referred from table result.

Cumulative plots: It shows the cumulative sum of bases of first x contigs ordered in descend.

Coverage histogram: It shows distribution of total contigs lengths at different coverage depths. peak at 15.5x of 1400kbp.
Future Directions:

    parsing predicted protein in gff
    create a file in FASTA format containing header (including protein annotations from gff) and coreresponding protein sequence, could use Bio.SeqRecords,Bio.Seq,Bio.SeqIO classes inside BioPython module to construct by iterating header and seq simultaneously using zip and write to file.
    Run BLAST against Swissprot database
    Retrieve BLAST output in which it contains SwissProt protein ID for each protein sequence
    Through UniProt we retrieve GO terms that map to SwissProt protein ID

References:

Bolger, Lohse, M., & Usadel, B. (2014). Trimmomatic: a flexible trimmer for Illumina sequence data. Bioinformatics (Oxford, England), 30(15), 2114–2120. https://doi.org/10.1093/bioinformatics/btu170

John Besemer, Alexandre Lomsadze, Mark Borodovsky, GeneMarkS: a self-training method for prediction of gene starts in microbial genomes. Implications for finding sequence motifs in regulatory regions, Nucleic Acids Research, Volume 29, Issue 12, 15 June 2001, Pages 2607–2618, https://doi.org/10.1093/nar/29.12.2607

Bankevich, A., Nurk, S., Antipov, D., Gurevich, A. A., Dvorkin, M., Kulikov, A. S., Lesin, V. M., Nikolenko, S. I., Pham, S., Prjibelski, A. D., Pyshkin, A. V., Sirotkin, A. V., Vyahhi, N., Tesler, G., Alekseyev, M. A., & Pevzner, P. A. (2012). SPAdes: a new genome assembly algorithm and its applications to single-cell sequencing. Journal of computational biology : a journal of computational molecular cell biology, 19(5), 455–477. https://doi.org/10.1089/cmb.2012.0021

Gurevich, A., Saveliev, V., Vyahhi, N., & Tesler, G. (2013). QUAST: quality assessment tool for genome assemblies. Bioinformatics (Oxford, England), 29(8), 1072–1075. https://doi.org/10.1093/bioinformatics/btt086

Helen Attrill, Pascale Gaudet, Rachael P Huntley, Ruth C Lovering, Stacia R Engel, Sylvain Poux, Kimberly M Van Auken, George Georghiou, Marcus C Chibucos, Tanya Z Berardini, Valerie Wood, Harold Drabkin, Petra Fey, Penelope Garmiri, Midori A Harris, Tony Sawford, Leonore Reiser, Rebecca Tauber, Sabrina Toro, The Gene Ontology Consortium, Annotation of gene product function from high-throughput studies using the Gene Ontology, Database, Volume 2019, 2019, baz007, https://doi.org/10.1093/database/baz007
