	#!/bin/bash -l

	export TMPDIR=tmp
	source ~/miniconda3/etc/profile.d/conda.sh
	conda activate blast
	line=$1
	blastn -query "$line" -subject reference.fasta -outfmt '6 std qlen' -out "$line"_pea_pectin_blastn_results.txt
