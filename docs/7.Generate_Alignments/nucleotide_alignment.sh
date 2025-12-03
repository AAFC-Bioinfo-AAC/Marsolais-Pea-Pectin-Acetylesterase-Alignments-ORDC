#!/bin/bash -l
	
export TMPDIR=tmp
source ~/miniconda3/etc/profile.d/conda.sh
conda activate pea_alignment
mafft all_blastn_sequences.fasta > blastn_multiple_alignment.fasta
mafft --addfragments reference_rev_comp.fasta --reorder blastn_multiple_alignment.fasta > reference_based_pea_alignment_blastn_mafft_rev_comp.fasta
