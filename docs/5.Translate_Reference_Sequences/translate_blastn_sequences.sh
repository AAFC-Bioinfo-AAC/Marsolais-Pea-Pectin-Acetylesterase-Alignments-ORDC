	#!/bin/bash -l

	
	source ~/miniconda3/etc/profile.d/conda.sh
	conda activate pea_alignment
	
	# Directory containing assembly files
	assembly_dir="~/Marsolais_Pea_Genome/0.Pea_Genomes/Pea_Sequences/blastn_headers/blastn_translate"
	
	# Directory to store translated protein sequences
	output_dir="~/Marsolais_Pea_Genome/0.Pea_Genomes/Pea_Sequences/blastn_headers/blastn_translate"
	
	# Loop through each assembly file
	for assembly_file in "${assembly_dir}"/*.scaffold.fasta_aligned_sequences_blastn.txt; do
	    # Extract the filename without extension
	    filename=$(basename "$assembly_file" .txt)
	            
	    # Translate the assembly file to protein sequence
	    transeq -sequence "$assembly_file" -outseq "${output_dir}/${filename}_protein_concatenate.fasta" -frame 6
	done
