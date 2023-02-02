import csv
from pathlib import Path

def profitloss_function():
    """
    When function is executed, the program will compute the difference in net profit between each day.
    It would return NET PROFIT SURPLUS or PROFIT DEFICIT depending on the values. If increment is equal to 0, 
    It would return NET PROFIT SURPLUS, otherwise it would return PROFIT DEFICIT. 
    """
    fp_summary = Path.cwd()/"igp_pfb"/"summary_report.txt" 
    file_path = Path.cwd()/"igp_pfb"/"csv_reports"/"profit-and-loss.csv"

    # Creates two variables assigns the value zero
    increment = 0
    shortage = 0

    # Creates an empty list 
    profitloss = []
    # Opening file in read mode with encoding "UTF-8"
    with file_path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
        reader = csv.reader(file)
        # Use 'next()' to skip the header 
        next(reader)

        for value in reader:
            profitloss.append(value)
            # Returns the number of items in an object, profitloss
            length = len(profitloss)
            # Iterates thorugh all the days 
            while increment + 1 < length:
                # Creates two variables and assigns values for previous day and current day 
                converted1 = int((profitloss[increment][4]))
                converted2 = int(profitloss[increment + 1][4])
                # Condition: Checks if current day is lesser than previous day 
                condition = converted1 >  converted2
                if condition: 
                    # Assigns the difference in values to deficit 
                    shortage = converted1 - converted2
                    # Opening file in append mode with encoding "UTF-8"
                    with fp_summary.open(mode="a", encoding = "UTF-8", newline = "") as file:
                        # Message to be appended on to the file
                        message = f"\n[PROFIT DEFICIT] DAY: {profitloss[increment + 1][0]}, AMOUNT: USD{(shortage)}"
                        file.write(message)   
                        # Closes the files    
                        file.close()
                # Adding one on every iteration
                increment += 1
            # if increment equals to 0 
        if increment == 0:
                # Opening file in append mode with encoding "UTF-8"
            with fp_summary.open(mode="a", encoding = "UTF-8", newline = "") as file:
                message = f"\n[NET PROFIT SURPLUS] net profit on each day is higher than the previous day"
                file.write(message.upper())
                # Closes the fp_summary file 
                file.close()
