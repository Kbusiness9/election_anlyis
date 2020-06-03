# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter
total_votes = 0

# candidate options
candidate_options = []
candidate_votes ={}

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here. 
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    #print(headers)
    
    for row in file_reader:
        # add the total vote count
        total_votes += 1
        # candidates name for each row
        candidate_name = row[2]

        # if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # add candidate name to the candidate list
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

print(total_votes)
print(candidate_options)
print(candidate_votes)

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate]
    # 3. Calculate the percentage of votes.
    vote_percentage = int(votes) / int(total_votes) * 100
    candidate_results = (
        f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
    )

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate

    # 4. Print the candidate name and percentage of votes.
    print(candidate_results)
    
   
    
    winning_candidate_summary = (
        f"------------\n"
        f"Winner: {winning_candidate}"
        f"Winning Vote Count {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------\n"
    )
print(winning_candidate_summary)
    
    # Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    election_result = (
        f"\nElection Results\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------\n"
    )
    print(election_result, end="")
    txt_file.write(election_result)




