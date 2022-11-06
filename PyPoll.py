from platform import python_branch
# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of cotes each candidate won.
# 5. The winner of the election based on popular vote.

#file_variable = open(filename, mode)

#Opening and reading files

#Direct

# Assign a variable for the file to load and the path.
##file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
##election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
##election_data.close()

##Indirect

#import
##import os

##import csv

#assign a variable for the file to load and the path.
##file_to_upload = os.path.join("Resources", "election_results.csv")

#Open the election results and read the file.
##with open(file_to_upload) as election_data:

    #Print the file object
    ##print(election_data)

###Read Election Results

#Add our dependencies.
import os
import csv

#Create a filename variable to a direct or indirect path to the file.
file_to_load = os.path.join("Resources", "election_results.csv")

#Using the open()  function with the "w" mode we will write data to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Setting vote count to 0 before each loop.
total_votes = 0

#Candidate List
candidate_options = []

#Creating candidate dictionary.
candidate_votes = {}

#Winning Candidate and Winning Count Tracker.
winning_candidate = ""

winning_count = 0

winning_percentage = 0

#Open election results and read the file.
with open(file_to_load) as election_data:

    #Read and analyze data here.
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Read the header row.
    headers  = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        
        #Add total vote count.
        total_votes += 1

        #Print Candidate's names.
        candidate_name = row[2]

        #If candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            #add candidate name to candidate list.
            candidate_options.append(candidate_name)

            #begin tracking vote count by setting to 0.
            candidate_votes[candidate_name] = 0

        #Track votes.
        candidate_votes[candidate_name] += 1

    #Print the total votes.
    ##print(total_votes)

    #Print candidate list.
    ##print(candidate_options)

    #Print Candidate Votes.
    ##print(candidate_votes)

##Determining percentage of votes.
#Iterate through the candidate list.
for candidate_name in candidate_votes:
    #Retreive vote count of a candidate.
    votes = candidate_votes[candidate_name]
    #Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100


    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        #            
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

        winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# To do: print out each candidate's name, vote count, and percentage of

# votes to the terminal.






    # Print each row in the CSV file.
    ##for row in file_reader:
        ##for i in range(len(row)):
            
            ##print([i])











#With Statement
##import os
##import csv

##file_to_save = os.path.join("analysis", "election_analysis.txt")

##with open(file_to_save, "w") as txt_file:

    ##txt_file.write("Hello World!")

    #Writing counties onto the text file
    ##txt_file.write("Counties in the Election\n---------------------\nArapahoe\nDenver\nJefferson")
