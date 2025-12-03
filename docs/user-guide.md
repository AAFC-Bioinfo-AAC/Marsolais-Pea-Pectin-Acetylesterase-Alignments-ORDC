# Marsolais-Pea-Pectin-Acetylesterase-Alignments-ORDC - USER GUIDE

## Table of Contents

- [Overview](#overview)
  - [Workflow Overview](#workflow-overview)
  - [Workflow diagram](#workflow-diagram)
- [Data](#data)
  - [Pea](#pea)
  - [Chickpea](#chickpea)
- [Software Requirements](#software-requirements)
- [Usage](#usage)
  - [1.Change Headers](#1change-headers)
  - [2.Getting Reverse Complement of Reference Sequence](#2getting-reverse-complement-of-reference-sequence)
  - [3.BLASTn](#3blastn)
  - [4.Extracting Aligned Sequences from BLASTn Results](#4extracting-aligned-sequences-from-blastn-results)
  - [5.Translating the Reference and Aligned Sequences from the Genomes](#5translating-the-reference-and-aligned-sequences-from-the-genomes)
  - [6.Concatenating the Aligned and Reference Sequences](#6concatenating-the-aligned-and-reference-sequences)
  - [7.Generating the Nucleotide and Protein Sequence Alignments](#7generating-the-nucleotide-and-protein-sequence-alignments)


## Overview

This project implements a pipeline for creating nucleotide and amino acid alignments using 118 pea genomes and a reference pectin acetylesterase gene. The workflow includes BLAST alignment, sequence extraction, translation, and concatenation steps to generate comprehensive sequence alignments for comparative genomics analysis.

### Workflow Overview
The pipeline consists of the following steps:

1. **Change Headers** - Standardizes FASTA headers for genome identification
2. **Reverse Complement** - Generates reverse complement of reference sequence
3. **BLASTn** - Performs nucleotide BLAST searches against reference
4. **Extract Sequences** - Extracts aligned sequences from BLAST results
5. **Translation** - Translates nucleotide sequences to amino acids
6. **Concatenation** - Concatenates multiple sequences per genome
7. **Alignment** - Generates final nucleotide and protein alignments
   
### Workflow Diagram
![Work FlowChart of GEnerating Alignments](Marsolais_Pea_alignments_flowchart.drawio%20(1).svg)

## Data
### Pea
1. Reference Sequence: \
   The fasta file for the reference sequence contains the entire sequence (introns and exons) of the pea Pectin acetylesterase gene from [here](https://urgi.versailles.inra.fr/jbrowse/gmod_jbrowse/?data=myData%2FPea%2FPsat_v1a%2Fdata&loc=chr4LG4%3A203842315..203856294&tracks=DNA%2Cannotation.v1a%2Cannotation.eugene&highlight=).
2. Pea Whole Genomes: \
   The fasta files for 118 whole genomes of three different pea species were taken from [Yang et al.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9534762/) and were retrieved from [zenodo](https://zenodo.org/api/records/6622578/files-archive). 
### Chickpea
1. Reference Sequence: \
   The fasta file for the reference sequence contains the entire sequence (introns and exons) of the chickpea Pectin acetylesterase gene from [here](https://phytozome-next.jgi.doe.gov/report/gene/Carietinum_v1_0/Ca_20559)
2. Chickpea Whole Genomes: \
   The fasta files for the 10 whole chickpea genomes were taken from [here](https://knowpulse.usask.ca/genome-assemblies?genus=Cicer) for Cicer arientinum (n=2) and from [Khan et al.](https://www.nature.com/articles/s41588-024-01760-4) (n=8) which were retrieved from [NCBI](https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA1043734).

## Software Requirements

- BLAST v2.14.1
- EMBOSS v6.6.0
- MAFFT v7.525
- SeqKit v2.8.0
  
## Usage 
### 1.Change Headers
This script (*change_headers_blastn.py*) changes the headers of the fasta files of all the pea whole genomes to be the name of the genome and a unique number starting at 1 for each fasta file. The change of the headers allows for the aligned sequences to be easily identifed as belong to partifular genomes within the output alignments.
### 2.Getting Reverse Complement of Reference Sequence
This script (*seqkit_ref.sh*) take the initial reference sequence and changes it to the reverse complememnt of the original sequence. This allows the reference sequence to be in the same orientation as the aligned sequences from the whole pea genomes in the output alignments. This is done using the seqkit package.
### 3.BLASTn
This directory includes two scripts: *blastn.sh* and *setup_blastn.sh*. The first script (*blastn.sh*) sets up the BLASTn with the reference sequence as the subject and the genome as the query. The second script (*setup_blastn.sh*) loops the BLASTn script over all the pea genomes. 
### 4.Extracting Aligned Sequences from BLASTn Results
This directory includes three script: *extract_aligned_sequences.py*, *extract_sequences_single_genome.sh*, and *setup_extract_sequences.sh*. The first script (*extract_aligned_sequences.py*) is a python script that does though the blastn results and gets the start and end location in the genomes for the sequence that aligns to the reference sequences and extracts it from the fasta file for the genome. The second script (*extract_sequences_single_genome.sh*) calls that python script for a genome and the third script (*setup_extract_sequences.sh*) loops the second sequence over all the genomes in the analysis. The outputs are fasta files with the aligned sequences from each of the genomes.

### 5.Translating the Reference and Aligned Sequences from the Genomes
This directory contains two scripts: *translate_blastn_sequences.sh* and *translate_ref_seq.sh*. These scripts translate the nucleotide sequences of the aligned sequences from the genomes and the reference sequence using the transeq command from the emboss package. This step is required if you want to generate a amino acid sequence alignment that corresponds to the nucleotide alignment. The output is fasta files that contain the amino acid sequences that coincide with the nucleotide sequences that align with the reference sequence for each genome as well as a fasta file with the translated sequences from the translation of the reference sequence.

### 6.Concatenating the Aligned and Reference Sequences
This directory contains *concatenate.py* and *concatenate_ref.py*. These two scripts concatenate the multiple protein sequences that are present in each fasta after the tranalation step into one continuous sequence in order to align them.\
The *concantenate_chickpea.py* is used to concatenate all the multiple protein sequences in each fasta for the chickpea genomes after the translation step and maintain a meaningful header for each sequence. \

### 7.Generating the Nucleotide and Protein Sequence Alignments
This directory contains two scripts: *nucleotide_alignment.sh* and *protein_alignment.sh*. The first script (*nucleotide_alignment.sh*) generates a nucleotide alignment of the reference sequence and the sequenced that aligned to it based on the BLASTn results. The second script (*protein_alignment.sh*) generates a amino acid alignment from the translated sequences. The alignments are generated with mafft. In order to generate the alignments, the input includes a single file (all_blastn_sequences.fasta for *nucleotide_alignment.sh* and multifasta_assemblies_concat.fasta for *protein_alignment.sh*) which contains all the sequences from the genomes which can be created using the *cat* command. This step generates your final outputs which consists of a nucleotide and a amino acid alignment of pectin acetylesterase from the pea genomes and the reference sequence.
## Output Files
1. A nucleotide sequence alignment
2. A protein sequence alignment
