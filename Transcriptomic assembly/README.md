-reference guided assembly
Merge bamfiles using samtools merge (1) by specifying -b to pass in bam txt file, which lists path to bam files from alignment. Run trinity (2) by indicating –genome_guided_bam, which tells trinity it is reference guided assembly and AipAll.bam is the merged bam file. –genome_guided_max_intron specifies the maximum separation distance Trinity will allow for segments of a transcript to span introns. –max_memory is the maximum memory Trinity will use for the assembly. 1> will redirect STDOUT to trinity.log, and 2> will redirect STDERR to trinity.err. Check assembly statistics by running TrinityStats.pl.

-De novo assembly
After building lists of left and right reads, they are passed to trinity (2)in the --left and --right. Passing sequence type --seqType fq 
and specifying output directory --output trinity_de-novo \
and max memory for this job --max_memory 10G --CPU 4.

-result
N50 for reference guided assembly is 574 based on all transcripts contigs and 506 based on only longest isoform pet gene. N50 for De Novo assembly is 617 based on all transcripts contigs and 504 based on only longest isoform.



1. Li, Handsaker, B., Wysoker, A., Fennell, T., Ruan, J., Homer, N., Marth, G., Abecasis, G., & Durbin, R. (2009). The Sequence Alignment/Map format and SAMtools. Bioinformatics, 25(16), 2078–2079. https://doi.org/10.1093/bioinformatics/btp352
2. Grabherr MG, Haas BJ, Yassour M, Levin JZ, Thompson DA, Amit I, Adiconis X, Fan L, Raychowdhury R, Zeng Q, Chen Z, Mauceli E, Hacohen N, Gnirke A, Rhind N, di Palma F, Birren BW, Nusbaum C, Lindblad-Toh K, Friedman N, Regev A. Full-length transcriptome assembly from RNA-seq data without a reference genome. Nat Biotechnol. 2011 May 15;29(7):644-52. doi: 10.1038/nbt.1883. PubMed PMID: 21572440.
