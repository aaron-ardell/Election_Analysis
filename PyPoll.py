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

#Open election results and read the file.
with open(file_to_load) as election_data:

    #Read and analyze data here.
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print the header row.
    headers  = next(file_reader)

    print(headers)


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
