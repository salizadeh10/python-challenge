# The total number of months included in the dataset - done 86
# The total net amount of "Profit/Losses" over the entire period - done - $38382578
# The average change in "Profit/Losses" between months over the entire period - $-2315.12
# The greatest increase in profits (date and amount) over the entire period - Feb-2012 ($1926159)
# The greatest decrease in losses (date and amount) over the entire period - Sep-2013 ($-2196167)

import os
import csv

# Path to collect data from the Resources folder
path = os.path.join('..', 'PyBank', 'budget_data.csv')

total_number_of_months = 0
total_profit_losses = 0
greatest_increase = 0
greatest_decrease = 0
periods_list = []
profit_loss_list = []
profit_loss_change_list = []
monthly_change = 0
monthly_change_sum = 0
change_total = 0
average_change = 0
max_increase_index = 0
min_increase_index = 0
max_increase = 0
min_increase = 0

# Read in the CSV file
with open(path, 'r', newline='' , encoding="UTF-8") as budget_data:

    # Split the data on commas
    csv_reader = csv.reader(budget_data, delimiter=',')
    
    header = next(csv_reader)
 
    # Loop through the data
    for row in csv_reader:

		# Count number of months - number of rows in the file
        total_number_of_months += 1
        total_profit_losses = total_profit_losses + int(row[1])
        
        # make lists of the periods and their associated P/L for later
        periods_list.append(str(row[0]))
        profit_loss_list.append(int(row[1]))

# Loop through the periods an associated P/L to calculate the average monthly P/L change
for i in range(int(total_number_of_months - 1)):
	monthly_change = (profit_loss_list[i + 1]) - (profit_loss_list[i])
	profit_loss_change_list.append(monthly_change)
	
# Calculate the average monthly changes in P/L
for nums in profit_loss_change_list:
	change_total += nums
	average_change = round(change_total / (total_number_of_months - 1), 2)

# Determine maximum increase on P/L across the periods
max = max(profit_loss_change_list)
max_increase_index = profit_loss_change_list.index(max)
max_increase = periods_list[max_increase_index + 1]

# Determine minimum increase on P/L across the periods
min = min(profit_loss_change_list)
min_increase_index = profit_loss_change_list.index(min)
min_increase = periods_list[min_increase_index + 1]

# Print results to terminal
print(f"Total Months: {total_number_of_months}")
print(f"Total Profit/Losses: ${total_profit_losses}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profit/Losses: {max_increase} ${max} ")
print(f"Greatest Decrease in Profit/Losses: {min_increase} ${min} ")

# Finally, write results to a txt file
path= os.path.join ('..' , 'PyBank' , 'budget_data.txt')

with open(path, "w") as text_file:

    print(f"Financial Analysis", file=text_file)
    print("---------------------------------", file=text_file)
    print("Total Months: " + str(total_number_of_months), file=text_file)
    print("Total Profit/Losses: $" + str(total_profit_losses), file=text_file)
    print("Average Change: $" + str(average_change), file=text_file)
    print("Greatest Increase in Profit/Losses: " + str(max_increase) + " $" + str(max), file=text_file)
    print("Greatest Decrease in Profit/Losses: " + str(min_increase) + " $" + str(min), file=text_file)
    #budget_data_txt.close()

