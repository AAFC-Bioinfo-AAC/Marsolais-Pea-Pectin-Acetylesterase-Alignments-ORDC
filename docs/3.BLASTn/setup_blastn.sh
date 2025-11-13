#!/bin/bash -l
cat "list_pea_assemblies_nucl.txt" | while IFS= read -r line; do
	          echo "Processing line: $line"
	          sbatch blast.sh "$line"
done
