#!/bin/bash -l
cat "list_pea_genomes.txt" | while IFS= read -r line; do
	            echo "Processing line: $line"
	            sbatch extract_sequences_single_genome.sh $line
	
done
