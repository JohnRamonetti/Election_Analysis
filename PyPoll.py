# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 


# Add our dependencies
import csv
import os
# Assign a variable for the file to load and it's path.
file_to_load = os.path.join('Resources','election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Initialize a total vote counter
total_votes = 0
# Initialize candidate list
candidate_options = []
# Initialize a dictionary to count votes for each candidate
candidate_votes = {}

# Initialize Winning candidate and Winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
 
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Iterate through each row in the csv file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # Print the candidate name for each row
        candidate_name = row[2]
        # Add the candidate name to the candidate list if it's not duplicative
        if candidate_name not in candidate_options:
            # add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # and begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add to the vote count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through counts
# Iterate through the candidate list
for candidate_name in candidate_votes:
    # retrieve vote count of the candidate
    votes = candidate_votes[candidate_name]
    # calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    # print the candidate name, perdentage of votes and vote count
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

# Print out the winning candidate, vote count and percentage to terminal
winning_candidate_summary = (
    f"---------------------------\n"
    f"Winner:  {winning_candidate}\n"
    f"Winning Vote Count:  {winning_count:,}\n"
    f"Winning Percentage:  {winning_percentage:.1f}%\n"
    f"---------------------------\n")
print(winning_candidate_summary)


   
    



# Using the open() function with the "w" mode we write data to the file
# with open(file_to_save,"w") as txt_file:

#     # Write some data to the file"
#     txt_file.write("Counties in the Election\n-------------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")
 




