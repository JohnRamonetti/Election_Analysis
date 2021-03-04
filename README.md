# Election Analysis

## Project Overview
We have been asked to perform an audit of the election results of a recent Colorado congressional election.  The goal is to see if we can use Python to automate this process in an efficient manner that can then be used on a much broader scale.  A Colorado Board of Elections employee has asked to include the following information in our election audit results.  
 1. The total number of votes cast
 2. A complete list of candidates who received votes
 3. The percentage of votes each candidate won
 4. The total number of votes each candidate won
 5. The winner of the election based on popular vote. 

A secondary/ followup task was added requesting that we include the following additional information in our analysis results.
 1. The voter turnout for each county
 2. The percentage of votes from each county, out of the total count
 3. The county with the highest turnout.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.7, Visual Studio Code 1.53.2

## Summary of [Results](Analysis/election_analysis.txt)

The [analysis](Analysis/screenshots/text_output.png) of the election shows that:
- There were 369,711 votes cast in the election.

- The candidates were:
    - Candidate 1: Charles Casper Stockham
    - Candidate 2: Diana DeGette
    - Candidate 3: Raymon Anthony Doane

 - The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote, or 85,213 votes.
    - Diana DeGette received 73.8% of the vote, or 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote, or 11,606 votes.

  - The winner of the election was:
    -  Diana DeGette, who received 73.8% of the vote and 272,892 votes.


The analysis shows the following for the secondary/followup task:
 - Voter turnout by county was:
    - Jefferson County accounted for 10.5% of the total vote count, for a total of 38,855 votes.
    - Denver County accounted for 82.8% of the total vote count, for a total of 306,055 votes.
    - Arapahoe County accounted for 6.7% of the total vote count, for a total of 24,801 votes.

  - The county with the highest voter turnout was
     -  Denver.


## Summary and Statement of Broader Application

### I think the Election Commission would be wise to consider using this Python approach to analyze, and record, election results on a much broader basis.  The algorithm used herein can be easily adapted to any election, and with python's ability to speedily process large quantities of data, the size of the election (i.e., vote count) is not an issue.  The output of this initial audit was designed to print to the [terminal](Analysis/screenshots/terminal_output.png) and to a [text file](Analysis/screenshots/text_output.png).  The [output here is just formatted text](Analysis/screenshots/Output_is_formatted_text.png).  To expand the utility of the algorithm, we'd send output to, for example, a .csv file rather than a [text file](Analysis/screenshots/save_to_text_file.png), so the analysis results are more accessible and easily tabulated at any time.  This would require some relatively simple changes to the [objects and variables used within the program](Analysis/screenshots/text_file_and_variables.png).  We would use more complex arrays, such as lists of dictionaries to store results for output to the .csv files rather than just to read raw data from our input file.
