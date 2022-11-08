# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1
  
## Overview of the Election Audit(Challenge)
The election commission has requested additional data to complete their audit of the election results.
  
  1. The voter turnout of each county.  
  2. The percentage of votes from each country out of the total count.  
  3. The county with the highest voter turnout.

## Process

To gather this additional data the following changes needed to be made to the existing code:

  1. We need **variables** to create a **list** of the county names and a **dictionary** to correlate the county names to vote count values. They're currently empty, but we'll be getting to that shortly.
  
`county_names = [], county_votes = {}`
 
  2. Even more **variables**, this time in preparation for calculating the largest turnouts by county. Largest turnout county is designated as a String value, while largest turnout vote and percentage are set up as numeric values.

`lar_tout_county = "",
lar_tout_vote = 0,
lar_tout_percentage = 0`

  3. We need to point out where the county data is within the provided .csv file. It's in the middle of three rows, so we'll designate it accordingly.

`     county = row[1]`

  4. Now we know where to loop to sort through the county names, let's go ahead and do it. We'll use the **"county_names" list** to store each unique name it pulls out of the middle row of data within the .csv file. If it's not already on the "county_names" list, the code will add it. While we're looping through the .csv data, we'll go ahead and pick up the votes counts tied to each county name.
```     
     if county not in county_names:       
        county_names.append(county)
        county_votes[county] = 0
```
  5. Let's add the vote counts to the "county_votes" dictionary. "County" being the **key** which the values are organized. "+=1" adding cumulative data output from the "if" conditional to county's total votes.

`        county_votes[county] += 1`

  6. **Our "county_votes" dictionary is complete!** But that only gets us the voter turn-out by county. Now we start looping through the dictionary to pull those total votes per county and start calculating turnout percentages. That's where the second set of variables are going to come into play. We'll create a **variable "cou_votes"** for the values of our "county_votes" dictionary. Utilize the existing **"total_votes" variable** from existing code and calculate out the percentage. An f-string statement to present the results of percentage calculations. Then, while still in our loop, we'll slip in an **if conditional** to catch the largest value of votes and percentages to designate the largest turnout.  That's it, we now have all our data.

    ```
    for county in county_votes:
        # 6b: Retrieve the county vote count.
        cou_votes = county_votes[county]
        # 6c: Calculate the percentage of votes for the county.
        cou_votes_percentage = float(cou_votes)/float(total_votes)*100        

         # 6d: Print the county results to the terminal.
       county_results = (f"{county}: {cou_votes_percentage:.1f}% ({cou_votes:,})\n")
         # 6e: Save the county votes to a text file.
        print(county_results)
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (cou_votes > lar_tout_vote) and (cou_votes_percentage > lar_tout_percentage):
            lar_tout_vote = cou_votes
            lar_tout_county = county
            lar_tout_percentage = cou_votes_percentage
            ```

  7. Now it's just a matter of adding the results to both the terminal and the written .txt file. We're adding some lines to break up the presentation of the data in both formats, and adding the **new line character "\n"** to ensure proper presentation in the .txt file.

```
    lar_tout_results = (
        f"-------------------------\n"
        f"Largest county turnout: {lar_tout_county}\n"
        f"-------------------------\n"
    )
    print(lar_tout_results)
```

  8. Finally, we're going to **write** the results variable onto the .txt file.

 `txt_file.write(lar_tout_results)`
 
 ## Election-Audit Results:
- There were **369,711** votes cast in the election.
- The candidates were:
  - **Charles Casper Stockham**  
  - **Diana DeGette**
  - **Raymon Anthony Doane**
- The candidate results were:
  - **Charles Casper Stockham** received **23.0%** of the vote and **85,213** number of votes.
  - **Diana DeGette** received **73.8%** of the vote and **272,892** number of votes.
  - **Raymon Anthony Doane** received **3.1%** of the vote and **11,606** number of votes. 
-The winner of the election was:
  - **Diana DeGette** received **73.8%** of the vote and **272,892** number of votes.
 
- The county-by-county breakdown of the votes were as follows:
  - **Jefferson** county had **10.5%** of the total votes or **38,855** number of votes.
  - **Denver** county had **82.8%** of the total votes or **306,055** numebr of votes.
  - **Arapahoe** county had **6.7%** of the total votes or **24,801** number of votes.
- **Denver** county had the **largest voter turnout**.
 
 ![This is an image](https://raw.githubusercontent.com/aaron-ardell/Election_Analysis/main/Pypoll_challenge_terminal.png)
 
 ## Challenge Summary
 
The source data's restriction of only three counties does not limit the number of counties this code can calculate. The variable designations for this code relate the nature of the source data file's information concerning counties. However, the code itself could be applied to any election's data of any scale or scope, whether precinct, zipcode, county, state or national. In fact, we can even add another layer of for-loops and if-statements to easily expand the thoroughness of this code at multiple scales(city/county, county/state, etc). Additional if-statement conditionals could be utilized to further sort demographic data.
 
 
