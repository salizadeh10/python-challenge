# You will be give a set of poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate. Y
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.


# As an example, your analysis should look similar to the one below:


#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
# -------------------------
#  Winner: Khan

import os
import csv

total_votes = 0
candidate_name = "" 
vote_count_for_candidate = 0
percentage = 0
all_candidates_list = []
unique_candidates_list = []
votes_for_candidate_list = []
percentage_votes_list = []

# Path to collect data from the Resources folder
path = os.path.join('..', 'PyPoll', 'election_data.csv')


# Read in the CSV file
with open(path, 'r', newline='' , encoding="UTF-8") as voting_results_data:

    # Split the data on commas
    csv_reader = csv.reader(voting_results_data, delimiter=',')
    
    header = next(csv_reader)
 
 	# loop through the file and count the number of votes cast and store candidate 
 	# names in list for later
    for row in csv_reader:
        total_votes += 1
        all_candidates_list.append(row[2])   
    
    print("total votes = " + str(total_votes))
    
	# Loop through the list of candidates and list the unique names
    for x in all_candidates_list:
        # check if exists in unique_list or not
        if x not in unique_candidates_list:
            unique_candidates_list.append(x)
    
    print("candidates are: " + str(unique_candidates_list))
    
    # count the votes for each candiate
    for i in range(len(unique_candidates_list)):

        for candidate_name in all_candidates_list:

            if candidate_name == unique_candidates_list[i]:
                vote_count_for_candidate +=1  
      
        votes_for_candidate_list.append(vote_count_for_candidate)
        vote_count_for_candidate = 0
        
print ("vote counts are: " + str(votes_for_candidate_list))

for votes in votes_for_candidate_list:
    percentage = float(votes/total_votes)*100
    #f=round(p,2)
    percentage_votes_list.append(str(round(percentage, 2))+"%")
    
print ("Percentage votes are: " + str(percentage_votes_list))


winner_max= max(votes_for_candidate_list)  
print ("winner max = " + str(winner_max))
winner_index=votes_for_candidate_list.index(winner_max)
print ("index = " + str(winner_max))
winner = unique_candidates_list[winner_index]
print ("winner = " + str(winner))

print("Election Results")
print("----------------------------")
print (f"Total Votes : {total_votes}")
print("----------------------------")
for i in range(4):
	print (unique_candidates_list[i] + " " + str(percentage_votes_list[i]) + "  (" + str(votes_for_candidate_list[i]) + ")")
print("----------------------------")
print("Winner: " + str(winner))

# Finally, write results to a txt file
path= os.path.join ('..' , 'PyPoll' , 'election_results.txt')

with open(path, "w") as text_file:
	print("Election Results", file=text_file)
	print("----------------------------", file=text_file)
	print (f"Total Votes : {total_votes}", file=text_file)
	print("----------------------------", file=text_file)
	for i in range(4):
		print (unique_candidates_list[i] + " " + str(percentage_votes_list[i]) + "  (" + str(votes_for_candidate_list[i]) + ")", file=text_file)
	print("----------------------------", file=text_file)
	print("Winner: " + str(winner), file=text_file)

