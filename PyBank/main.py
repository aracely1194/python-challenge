# Importing Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "/Users/aracelyvivanco/Desktop/Bootcamp/Homework_Folder/HW3/PyBank", "budget_data.csv")

# Create lists to parse data into
months = []
revenue =[]

# Read the CSV into pyBank and break up rows into seperate lists
with open(csvpath) as csvfile:
    pyBank = csv.reader(csvfile, delimiter=",")

    next(pyBank, None)
    for row in pyBank:
        months.append(row[0])
        revenue.append(int(row[1]))

# Find number of months by using len function
number_months = len(months)

# Find total revenue
total_revenue = 0

for row in range(len(revenue)):
    total_revenue = total_revenue + revenue[row]

# Find average change of profit
average_change = round(total_revenue/number_months,2)


# Find greatest increase and decrease in revenue profit
greatest_increase = 0
greatest_decrease = 0

for row in range(len(revenue)):
    if revenue[row] > greatest_increase:
        greatest_increase = revenue[row]
        increase_month = months[row]
    elif revenue[row] < greatest_decrease:
        greatest_decrease = revenue[row]
        decrease_month = months[row] 


# Set path for output file
output_path = os.path.join("..", "/Users/aracelyvivanco/Desktop/Bootcamp/Homework_Folder/HW3/PyBank", "output.txt")


# Open file and write summary into it
with open(output_path, 'w') as output_file:
    output_file.write('Financial Analysis \n')
    output_file.write('---------------------------- \n')
    output_file.writelines('Total Months: ' + str(number_months) + '\n')
    output_file.writelines('Net Total Revenue: ' + str(total_revenue) + '\n')
    output_file.writelines('Greatest Increase in Profits: ' + increase_month + ' (' + str(greatest_increase) + ')' + '\n')
    output_file.writelines('Greatest Decrease in Profits: ' + decrease_month + ' (' + str(greatest_decrease) + ')' + '\n')

# Open new text file and print summary on terminal
with open(output_path) as summary:
    print(summary.read())
