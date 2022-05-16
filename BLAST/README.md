BLAST files scripts: 
## blastPep.sh (Align Protein (from the ORFs) to SwissProt) 
-Running blastp to -query ORF to -db swissport specifying -max_target_seqs 1, -outfmt 6, threshold -evalue 1e-5, -num_treads 4, output to blastp.outfmt6,blastp.err 

## pfamScan.sh (Run hmmscan to find protein domains) 
-Running hmmscan from ORF, --cpu 4, ---domtblout pfam.domtblout, use query sequence to search the target database of profiles in hmm_db, and output ranked lists of the profiles with the most significant matches to the sequence, output to pfamScan.log, pfamScan.err 
 
## predictProteins.sh (Predict proteins) 
-Running transdecoder.predict specifying -t trinity_de-novo/Trinity.fasta, --retain_pfam_hits pfam.domtblout, --retain_blastp_hits blastp.outfmt6, output to predict.log, predict.err

## alignPredicted.sh (align predicted proteins) 
-Running blastp to -query Trinity.fasta.transdecoder.pep ORF to -db swissport, specifying -outfmt "6 qseqid sacc qlen slen length nident pident evalue stitle", thresh    old -evalue 1e-10, -num_treads 4 output to alignPredicted.txt, alignPredicted.err 
