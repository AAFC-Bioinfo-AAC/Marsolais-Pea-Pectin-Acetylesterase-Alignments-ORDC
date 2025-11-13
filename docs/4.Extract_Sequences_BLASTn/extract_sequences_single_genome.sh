	#!/bin/bash -l

	line=$1
	echo "$line"
	# Define the Python script
	python_script="extract_aligned_sequences.py"
	# Input files
	blast_results_file=$(printf "%s_pea_pectin_blastn_results.txt" "$line")
	echo "$blast_results_file"
	assembly_file="$line"
	echo "$assembly_file"
	# Output file
	output_file=$(printf "%s_aligned_sequences_blastn.txt" "$line")
	echo "$output_file"
	# Call the Python script with arguments
	python "$python_script" "$assembly_file" "$blast_results_file" "$output_file"
