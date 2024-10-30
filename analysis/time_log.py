import glob
import re
import os
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
