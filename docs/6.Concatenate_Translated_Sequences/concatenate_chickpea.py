import os

def concatenate_sequences(input_file, output_file):
    sequences = {}
    with open(input_file, 'r') as f:
        current_header = None
        current_sequence = ''
        for line in f:
            if line.startswith('>'):
                if current_header:
                    sequences.setdefault(current_header, []).append(current_sequence)
                # Extract all parts before the 4th underscore
                header_parts = line.strip()[1:].split('_')
                current_header = '_'.join(header_parts[:4])
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
    input_dir = "/gpfs/fs7/grdi/genarcc/wp3/hsanderson/Frederic_Chickpea/3.blastn_translate"
    output_dir = "/gpfs/fs7/grdi/genarcc/wp3/hsanderson/Frederic_Chickpea/4.blastn_translate_concat"

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

            # Process each input file in the directory
    for filename in os.listdir(input_dir):
        if filename.endswith("_aligned_sequences_blastn_protein.fasta"):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, filename.replace(".fasta", "_concatenated.fasta"))
            concatenate_sequences(input_file, output_file)
            print(f"Processed {filename}")
