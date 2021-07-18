# main.py /c/Users/15303/OneDrive/Desktop/python-challenge/PyBank
# From LINK: https://wonderful-data-c75b08.netlify.app/03-python/challenges/challenge/

# Your task is to create a Python script that analyzes the records to calculate each of the following:
# 1 The total number of months included in the dataset 
# 2 The net total amount of “Profit/Losses” over the entire period
# 3 Calculate the changes in “Profit/Losses” over the entire period, then find the average of those changes
# 4 The greatest increase in profits (date and amount) over the entire period
# 5 The greatest decrease in losses (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:

#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)

# 6 In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Inspired by Wonderful Data Python Day-03 Activity 08 'Wrestling with Functions' 
# LINK: https://wonderful-data-c75b08.netlify.app/03-python/activities/day-03/wrestling_with_functions/

# First, import os and csv 
import csv
import os


# Second, set file path for csv
# Create file_to_load and file to output
# Filepath Git Bash: 
#/c/Users/15303/OneDrive/Desktop/python-challenge/PyBank/Resources/budget_data.csv
file_to_load = os.path.join('Resources', 'budget_data.csv')



# Set up parameters
month_of_change = []
total_months = 0
net_change = [] 
greatest_increase = []
greatest_decrease = []
total_net = 0


# NOTE: the Total number of months printed to the terminal is 87, which is wrong
# This error is due to the fact that the line of code meant to skip the header does not work 
with open(file_to_load) as file_to_load:
    csvreader = csv.reader(file_to_load)
    header = next(file_to_load)
    
    
    total_months = 0 
    for row in file_to_load:
        total_months +=1
        
file_to_output = print(
    f"Total Months: {total_months}"    
)

print(file_to_output)


# The following code is based on Python Day 02 Activity 10 Write CSV Instructor Turn
# Specify the file to write to
file_to_output = os.path.join('analysis', 'financial_analysis.txt')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(file_to_output, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Months', 'Total', 'Average  Change',
                        'Greatest Increase in Profits', 'Greatest Decrease in Profits'])

    # Write the second row
    csvwriter.writerow([f'{total_months}, {net_change}, {net_change}, {greatest_increase}, {greatest_decrease}'])


# The following code is based on LINK: https://www.easytweaks.com/python-write-to-text-file/
#file_to_output = open('analysis', 'financial_analysis.txt')
#file_to_output.write(f"Total Months: {total_months}")
#file_to_output.close

# The following code is based on the Python Day 02 Activity 12 Student Activity Udemy Zip

# Zip lists together
# = zip(title, price, subscribers, reviews, review_percent, length)

# Set variable for output file
#output_file = os.path.join("web_final.csv")
#file_to_output = os.path.join('analysis', 'financial_analysis.txt')

#  Open the output file
#with open("file_to_output") as datafile:
    #writer = csv.writer(datafile)

    # Write the header row
    #writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                    # "Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    #writer.writerows(cleaned_csv)


# Third, define function 
#print_file_to_output(file_to_load):

    # Fourth, define months and total_months
    #months = str(budget_data[0])
    #total_months = int(budget_data[0])
    
    # Fifth, define profit_losses, total
    #profit_losses = int(budget_data[1])
    #total = 
    
    # Sixth, define
    
    
    
  
 # Total matches can be found by adding wins, losses, and draws together
    #total_matches = wins + losses + draws

    # Win percent can be found by dividing the the total wins by the total matches and multiplying by 100
    #win_percent = (wins / total_matches) * 100

    # Loss percent can be found by dividing the total losses by the total matches and multiplying by 100
    #loss_percent = (losses / total_matches) * 100

    # Draw percent can be found by dividing the total draws by the total matches and multiplying by 100
    #draw_percent = (draws / total_matches) * 100

 

    # Print out the Financial Analysis and Export financial_analysis.txt
    #print(f"Financial Analysis")
    #print(f"----------------------")
    #print(f"Total Months: {count_months}")
    #print(f"Total: {loss_percent}")
    #print(f"Average Change: {draw_percent}")
    #print(f"Greatest Increase in Profits: {draw_percent}")
    #print(f"Greatest Decrease in Profits: {draw_percent}")


# Read in the CSV file
#with open(budget_data_csv, 'r') as csvfile:

    # Split the data on commas
 #   csvreader = csv.reader(csvfile, delimiter=',')
  #  header = next(csvreader)

    # Loop through the data
    #for row in csvreader:
###

####

# The following code is based on work from Wayne Odd, Constantin C., and Drew
#print(f"Financial Analysis")
#print("-",*25)
#print(f"Total Months: {TotalMonths}")
#print(f"Total: ${Total}")
#print(f"Average Change: ${AverageChange}")
#print(f"Greatest Increase In Profits: {profinc} (${fmaxchange})")
#print(f"Greatest Decrease In Profits: {profdec} (${fminchange})")
#
# ???Csv = zip([[totalMonths, totalAmount, totalChange, avgChange, profinc, maxChange, profdec, minChange]])
# ??ut_path = os.path.join(".", "Analysis", "PyBank_Results.txt")
# ??? open(output_path, 'w', newline='') as csvfile: 
# ???csvwriter = csv.writer(csvfile, delimiter = ' ')
# ???csvwriter2 = csv.writer(csvfile, delimiter = ',')
#???csvwriter.writerows(["Total Months", "Total Profit", "Average Change", "Increase Month", "Greatest Increase In Profits", "Greatest Decrease In Profits",  ])
#



