#!/usr/bin/bash

# step 1:mafft used for sequence alignment
mafft

# step 2:aliview used for sequence curation and inspection
aliview aligned_seq_final.fasta

# step 3:iqtree used for tree generation
iqtree -s aligned_seq_final.fasta -m MFP -B 1000

# step 4:figtree used for tree visualization
figtree aligned_seq_final.fasta.treefile
