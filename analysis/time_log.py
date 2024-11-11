import glob
import re
import os
from datetime import datetime
from functions import *

# File paths
output_path = path + "/outputs"
steps_file = output_path + "/steps.txt"



with open(steps_file, 'w') as output_file:
    
    for filename in glob.glob(output_path + '/output*'):
        # Extract test number from the filename
        test_match = re.search(r"output_(\d+)_T_", os.path.basename(filename))
        if test_match:
            test_number = test_match.group(1)
        else:
            
            print(f"No test number found in filename: {filename}")
            continue

        with open(filename, 'r') as file:
            for line in file:
                # Search for the line pattern using regex
                match = re.search(r"Step number (\d+) performed on (.+)", line)
                if match:
                    
                    step_number = match.group(1)
                    timestamp = match.group(2)
                    
                    output_line = f"{timestamp}    Test {test_number}    {step_number}\n"

                    output_file.write(output_line)

print(f"Timestamp summary written to {steps_file}")

input_file = steps_file  
output_file = output_path + "/steps_sorted.txt"

# Read, parse, and sort the data
data_lines = []

# Open and read the input file
with open(input_file, 'r') as file:
    for line in file:
        # Split the line by whitespace and re-join for date and time parsing
        parts = line.split()
        timestamp = " ".join(parts[:4])  # Extract timestamp part
        test_label = parts[5]            # Extract test label (e.g., Test 2)
        step_number = parts[6]           # Extract step number
        
        # Convert timestamp to a datetime object for sorting
        dt_obj = datetime.strptime(timestamp, "%a %b %d %H:%M:%S")
        
        # Append to list as tuple (datetime object, original line)
        data_lines.append((dt_obj, line.strip()))

# Sort data based on datetime object
data_lines.sort(key=lambda x: x[0])

# Write sorted data to a new output file
with open(output_file, 'w') as file:
    for _, line in data_lines:
        file.write(line + '\n')

print("Data has been sorted and written to", output_file)
