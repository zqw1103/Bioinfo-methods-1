cut -f15 proteins.tsv | \
perl -ne '@list=split/\|/, $_; foreach my $i (@list){ print "$i\n"; }' | \
sort | uniq -c | sort -k1 -rn >path_ids.txt