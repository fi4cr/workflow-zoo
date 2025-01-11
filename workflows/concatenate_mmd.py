import glob
import os

# Get all .mmd files in current directory
mmd_files = glob.glob('*.mmd')

# Sort files alphabetically for consistent output
mmd_files.sort()

# Create output file
with open('concatenated_output.txt', 'w') as outfile:
    # Process each .mmd file
    for mmd_file in mmd_files:
        # Write file name as header
        outfile.write(f"\n{'='*50}\n")
        outfile.write(f"File: {mmd_file}\n")
        outfile.write(f"{'='*50}\n\n")
        
        # Read and write content of current file
        with open(mmd_file, 'r') as infile:
            outfile.write(infile.read())
            
        # Add newline between files
        outfile.write('\n')

print("Concatenation complete. Output saved to 'concatenated_output.txt'")
