import os
import csv

# Path to collect data from the Resources folder
input_file = os.path.join("Resources/budget_data.csv")
output_file = os.path.join("Resources/budget_data_out.csv")

Months = []
PnL = []
Diff = []
Output = []

#variables to keep track of max profit and loss and the month it occured
maxProfit = 0.00
maxLoss = 0.00
maxDiff = 0.00
minDiff = 0.00

maxProfitMonth = ''
maxLossMonth = ''
maxDiffMonth = ''
minDiffMonth = ''

# Read in the CSV file
with open(input_file, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    csv_header = next(csvreader)

    # Loop through the data and store in lists
    for row in csvreader:

        pnl = float(row[1])
        month = row[0]

        Months.append(month)
        PnL.append(pnl)
        
        #keep track of max profit
        if pnl > maxProfit:
            maxProfit = pnl
            maxProfitMonth = month

        #keep track of max Loss
        if pnl < maxLoss:
            maxLoss = pnl
            maxLossMonth = month
        
 # loop through the PnL list to figure out which month the greatest increase/decrease happened       
for i in range(1,len(PnL)):

    diff = PnL[i] - PnL[i-1]

    Diff.append(diff)

    if diff > maxDiff:
        maxDiff = diff
        maxDiffMonth = Months[i]

    if diff < minDiff:
        minDiff = diff
        minDiffMonth = Months[i]
        

Output.append('Financial Analysis')
Output.append('----------------------------')
Output.append(f'Total Months: {len(Months)}')
Output.append(f'Total: ${round(sum(PnL),2)}')
Output.append(f'Average  PnL: $ {round(sum(PnL)/len(PnL),2)}')
Output.append(f'Greatest Profit: {maxProfitMonth} (${round(maxProfit,2)})')
Output.append(f'Greatest Loss: {maxLossMonth} (${round(maxLoss, 2)})')
Output.append(f'Average change: {round(sum(Diff)/len(Diff),2)}')
Output.append(f'Greatest Increase in Profits: {maxDiffMonth} (${round(maxDiff,2)})')
Output.append(f'Greatest Decrease in Profits: {minDiffMonth} (${round(minDiff,2)})')


with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\n')
    csvwriter.writerow(Output)

for i in range(len(Output)):
    print(Output[i])
    

