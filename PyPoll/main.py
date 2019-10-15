import os
import csv

# Path to collect data from the Resources folder
input_file = os.path.join("Resources/election_data.csv")
output_file = os.path.join("Resources/election_data_out.csv")

Results = []
Candidates = []
maxVotes = 0
Output = []

# Read in the CSV file
with open(input_file, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    csv_header = next(csvreader)

    # Loop through the data and store in lists
    for row in csvreader:
        Results.append(row[2])

#create unique list of candidates
Candidates = list(set(Results))

#totalVotes
totalVotes = len(Results)

Output.append('Election Results')
Output.append('-----------------------')
Output.append(f'Total Votes: {totalVotes}')
Output.append('-----------------------')

for c in range(len(Candidates)):
    Output.append(f'{Candidates[c]}: {round(Results.count(Candidates[c])/totalVotes*100,3)}% ({Results.count(Candidates[c])})')
    if Results.count(Candidates[c]) > maxVotes:
        maxVotes = Results.count(Candidates[c])
        winner = Candidates[c]
        

Output.append('-----------------------')
Output.append(f'Winner: {winner}')

with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\n')
    csvwriter.writerow(Output)

for i in range(len(Output)):
    print(Output[i])