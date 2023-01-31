import csv
from pathlib import Path

def overheads_function():
    # Assigning a variable to file path of current working directory 
    file_path = Path.cwd()/"igp_pfb"/"csv_reports"/"overheads.csv"
    # Assigning a variable to file path of directory that would be appended
    fp_summary = Path.cwd()/"igp_pfb"/"summary_report.txt"
    
    # Initialize variables to store max overheads value and category
    max_overheads = 0
    max_category = ""

    # Opening file in read mode with encoding "UTF-8" 
    with file_path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
        # Instantiate a reader object
        reader = csv.reader(file)
        # Use 'next()' to skip the header
        next(reader)
        # Iterate over the lines of the csv file (processes each line)
        for line in reader:
            # Assigns float value to overheads
            overheads = float(line[1])
            # Check if overheads is greater than max_overheads, if yes update max_overheads and max_category
            if overheads > max_overheads:
                max_overheads = overheads
                max_category = line[0]

    # Opening file in append mode with encoding "UTF-8" 
    with fp_summary.open(mode = "a", encoding = "UTF-8", newline = "") as file:
        # Assigning the variable message to the final statement that is meant to be displayed on the final text file
        message = f"[HIGHEST OVERHEADS] {max_category}: {max_overheads}%"
        # Writing data to the final text file in uppercase
        file.write(message.upper())
    # Use '.close()' to close a file
    file.close()
