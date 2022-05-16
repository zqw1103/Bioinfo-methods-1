KEGG and GO procedures using Swissprot ID from BLAST output: 
## get_kegg_ids.py 
-Open the BLAST output, Iterate over each line of BLAST output, one by one, parsing uniprot ids and passing to KEGG API to retrieve KEGG ID.

## get_ko.py
-Open the KEGG to KO mappings, Iterate over lines of KEGG IDs, parsing KEGG ids and passing to KEGG api to retrieve KO.

## get_path.py 
-Open KO txt, Iterate over lines of the KEGG to KO mapping file, parsing KO IDs and passing to KEGG api to retrieve pathway IDs.

## getPathDesc.sh 
-Retrieve all pathway descriptions.

## mergeAll.R
-merge all tabular output and reformat to a single table.
