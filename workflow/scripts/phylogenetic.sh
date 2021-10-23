#!/usr/bin/bash

# step 1:mafft used for sequence alignment
mafft

# step 2:iqtree used for tree generation
iqtree -s aligned_seq_final.fasta -m MFP -B 1000

# step 3:figtree used for tree visualization
figtree aligned_seq_final.fasta.treefile
