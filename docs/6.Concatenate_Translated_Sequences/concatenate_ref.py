	def concatenate_sequences(input_file, output_file):
	    sequences = {}
	    with open(input_file, 'r') as f:
	        current_header = None
	        current_sequence = ''
	        for line in f:
	            if line.startswith('>'):
	                if current_header:
	                    sequences.setdefault(current_header, []).append(current_sequence)
	                current_header = line.strip()[1:].split('_')[0]  # Extract header prefix
	                current_sequence = ''
	            else:
	                current_sequence += line.strip()
	        if current_header:
	            sequences.setdefault(current_header, []).append(current_sequence)
	
	    with open(output_file, 'w') as f_out:
	        for header, seq_list in sequences.items():
	            concatenated_seq = ''.join(seq_list)
	            f_out.write(f'>{header}\n{concatenated_seq}\n')
	
	
	if __name__ == "__main__":
	    input_dir = "/gpfs/fs7/grdi/genarcc/wp3/hsanderson/Marsolais_Pea_Genome/0.Pea_Genomes/Pea_Sequences/blastn_headers/blastn_translate"
	    output_dir = "/gpfs/fs7/grdi/genarcc/wp3/hsanderson/Marsolais_Pea_Genome/0.Pea_Genomes/Pea_Sequences/blastn_headers/blastn_translate"
	
	    # Ensure output directory exists
	    os.makedirs(output_dir, exist_ok=True)
	
	    # Process each input file in the directory
	    for filename in os.listdir(input_dir):
	        if filename.endswith("_rev_comp_protein.fasta"):
	            input_file = os.path.join(input_dir, filename)
	            output_file = os.path.join(output_dir, filename.replace(".fasta", "_concatenated.fasta"))
	            concatenate_sequences(input_file, output_file)
	            print(f"Processed {filename}")
