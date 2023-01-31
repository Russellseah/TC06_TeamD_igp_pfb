import csv
from pathlib import Path

def coh_function():
    """
    When function is executed, the program will compute the difference in cash-on-hand between each day.
    It would return CASH SURPLUS or CASH DEFICIT depending on the values. If deficit is equal to 0, 
    It would return CASH SURPLUS, otherwise it would return CASH DEFICIT. 
    """
    # Assign file path of current working directory 
    file_path = Path.cwd() / "igp_pfb" / "csv_reports" / "cash-on-hand.csv"
    # Assign file path of directory that would be appended
    fp_summary = Path.cwd() / "igp_pfb" / "summary_report.txt"

    # Creates two variables, increment & deficit
    increment = 0
    deficit = 0
    # Creates empty list  
    cash_on_hand = []

    # Opens files with .open() with read mode to return a file object 
    with file_path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
        # Instantiate a reader object
        reader = csv.reader(file)
        # Return the next item from the iterator 
        next(reader)

        for value in reader:
            cash_on_hand.append(value)
        # Returns the number of items in the reader object
        length = len(cash_on_hand)
        # Iterates through one line and then the next line after first round of iteration. 
        while increment + 1 < length: 
            # Creates two variables, value1 & value2 assigning values of previous and current day
            value1 = int((cash_on_hand[increment][1]))
            value2 = int(cash_on_hand[increment + 1][1])
            # Checks if previous day value is greater than current day
            condition = value1 >  value2
            # Deficit will be calculated if condition is met
            if condition:
                deficit = value1 -  value2
                # Opening file in append mode with encoding "UTF-8" to return a file object
                with fp_summary.open(mode="a", encoding = "UTF-8", newline = "") as file:
                # Writes a message in the file
                    message = f"\n[CASH DEFICIT] DAY: {cash_on_hand[increment + 1][0]}, AMOUNT: USD{(deficit)}"
                    # Writes the message, above in the file
                    file.write(message.upper())
            # Adding one on every iteration, until last iteration
            increment += 1
        # If deficit equals to 0
        if deficit == 0:
            # Opening file in append mode with encoding "UTF-8"
            with fp_summary.open(mode="a", encoding = "UTF-8", newline = "") as file:
                message = (f"\n[CASH SURPLUS] cash on hand is higher than the pervious day")
                # Writes the message in the file with upper case
                file.write(message.upper())
            # Use '.close()' to close a file
            file.close()    

    # Use '.close()' to close a file
    file.close() 
