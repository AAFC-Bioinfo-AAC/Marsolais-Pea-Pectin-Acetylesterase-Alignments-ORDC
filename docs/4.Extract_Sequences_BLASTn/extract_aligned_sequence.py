	import sys
	
	def extract_aligned_sequences(assembly_file, blast_results_file, output_file):
	    # Read the assembly sequences into a dictionary
	    assembly_sequences = {}
	    current_sequence_id = None
	    with open(assembly_file) as assembly:
	        for line in assembly:
	            if line.startswith('>'):
	                if current_sequence_id is not None:
	                    assembly_sequences[current_sequence_id] = ''.join(current_sequence)
	                current_sequence_id = line.strip()[1:]
	                current_sequence = []
	            else:
	                current_sequence.append(line.strip())
	        if current_sequence_id is not None:
	            assembly_sequences[current_sequence_id] = ''.join(current_sequence)
	
	    # Process BLAST results and extract aligned sequences
	    aligned_sequences = {}
	    with open(blast_results_file) as blast_results:
	        for line in blast_results:
	            fields = line.strip().split()
	            if len(fields) >= 12:
	                subject_id = fields[0]
	                if subject_id in assembly_sequences:
	                    start_query, end_query = int(fields[6]), int(fields[7])
	                    aligned_sequence = assembly_sequences[subject_id][start_query-1:end_query]
	                    aligned_sequences[subject_id] = aligned_sequence
	
	    # Write aligned sequences to output file
	    with open(output_file, 'w') as output:
	        for subject_id, sequence in aligned_sequences.items():
	            output.write(f'>{subject_id}\n')
	            output.write(f'{sequence}\n')
	
	if __name__ == "__main__":
	    # Check if the correct number of command-line arguments are provided
	    if len(sys.argv) != 4:
	        print("Usage: python extract_aligned_sequences.py assembly_file blast_results_file output_file")
	        sys.exit(1)
	
	    # Extract command-line arguments
	    assembly_file = sys.argv[1]
	    blast_results_file = sys.argv[2]
	    output_file = sys.argv[3]
	
	    # Call the function with the provided arguments
    extract_aligned_sequences(assembly_file, blast_results_file, output_file)
