# Importing Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "/Users/aracelyvivanco/Desktop/Bootcamp/Homework_Folder/HW3/PyRoll", "election_data.csv")

# Definie things needed
candidates = []
total_votes = 0

# Read the CSV into pyBank
with open(csvpath) as csvfile:
    pyRoll = csv.reader(csvfile, delimiter=",")

# Loop through rows to get total votes and assign candidates to its own list
    for row in pyRoll:
        candidates.append(row[2])
        total_votes = total_votes + 1

# Sort candaitate list and then find unique candidates
sorted_candidates = sorted(candidates)
unique_candidates = []

for i in range(len(sorted_candidates)):
    if sorted_candidates[i - 1] != sorted_candidates[i]:
        unique_candidates.append(sorted_candidates[i])

#print(unique_candidates)

# Find total votes and percentage per candidate, assign total votes as float so division can work
candidate_voter_total = []
candidate_percentage = []
total_votes = float(total_votes-1)

for j in range(len(unique_candidates)):
    voter_count = 0

    for k in range(len(sorted_candidates)):
        if unique_candidates[j] == sorted_candidates[k]:
            voter_count += 1

    candidate_voter_total.append(voter_count)
    candidate_percentage.append(round((voter_count/total_votes)*100,2))

# Use zip to map all my lists and read into one main summary list
summary_list = []

mapped_results = zip(unique_candidates ,candidate_percentage ,candidate_voter_total)

for row in mapped_results:
    summary = (row[0] + ": ", str(row[1]) + "%", " (" + str(row[2]) + ")")
    summary_list.append(summary)

# Delete "Candidate" entry in list
#print(summary_list)
del summary_list[0]
#print(summary_list)


# Find winning candidate

for l in range(len(candidate_percentage)):
    if candidate_voter_total[l] > candidate_voter_total[l - 1]:
        winner = unique_candidates[l]


# Set path for output file
output_path = os.path.join("..", "/Users/aracelyvivanco/Desktop/Bootcamp/Homework_Folder/HW3/PyRoll", "output.txt")

total_votes = int(total_votes)
# Open file and write summary into it
with open(output_path, 'w') as output_file:
    output_file.write('---------------------------- \n')
    output_file.write('Election Results \n')
    output_file.write('---------------------------- \n')
    output_file.writelines('Total Votes:: ' + str(total_votes) + '\n')
    output_file.write('---------------------------- \n')
    for n in summary_list:
        output_file.write(str(n) + '\n')
    output_file.write('---------------------------- \n')
    output_file.writelines('Winner:: ' + winner + '\n')
    output_file.write('---------------------------- \n')


# Open new text file and print summary on terminal
with open(output_path) as summary:
    print(summary.read())