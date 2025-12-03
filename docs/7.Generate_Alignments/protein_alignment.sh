#!/bin/bash -l

	
export TMPDIR=tmp
source ~/miniconda3/etc/profile.d/conda.sh
conda activate pea_alignment
mafft multifasta_assemblies_concat.fasta > pea_alignment_blastn_protein_mafft_concat.fasta
mafft --addfragments reference_rev_comp_protein_concatenated.fasta --reorder pea_alignment_blastn_protein_mafft_concat.fasta > reference_based_pea_alignment_mafft_protein_rev_comp_concat.fasta
