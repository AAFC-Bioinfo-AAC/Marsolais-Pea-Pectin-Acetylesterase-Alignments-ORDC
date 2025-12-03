	import os
	
	def change_headers(input_file, output_file):
	    with open(input_file, 'r') as f:
	        lines = f.readlines()
	
	    # Initialize a counter for each filename
	    counter_dict = {}
	
	    with open(output_file, 'w') as f_out:
	        for line in lines:
	            if line.startswith('>'):
	                # Extract filename
	                filename = os.path.basename(input_file)
	                
	                # Increment counter for the filename
	                if filename not in counter_dict:
	                    counter_dict[filename] = 1
	                else:
	                    counter_dict[filename] += 1
	                
	                # Modify header
	                new_header = f'>{filename}_{counter_dict[filename]}\n'
	                f_out.write(new_header)
	            else:
	                # Write sequence
	                f_out.write(line)
	
	if __name__ == "__main__":
	    input_dir = "~/Marsolais_Pea_Genome/0.Pea_Genomes/Pea_Sequences"
	    output_dir = "~/Marsolais_Pea_Genome/0.Pea_Genomes/Pea_Sequences/headers"
	
	    # Ensure output directory exists
	    os.makedirs(output_dir, exist_ok=True)
	
	    # Process each input file in the directory
	    for filename in os.listdir(input_dir):
	        if filename.endswith(".fasta"):
	            input_file = os.path.join(input_dir, filename)
	            output_file = os.path.join(output_dir, filename)
	            change_headers(input_file, output_file)
	            print(f"Processed {filename}")
