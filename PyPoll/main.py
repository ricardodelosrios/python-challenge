#Import from operative system an csv file
import os
import csv

# Path to collect data from the Resources folder
election_data_csv = "PyPoll\Resources\election_data.csv"

#declare the variables
total_votes = 0
Char_Cas_Sto_votes=0
Dia_DeG_votes=0
Ray_Ant_Doa_votes=0
Porcentage_Char_Cas_Sto_votes=0
Porcentage_Dia_DeG_votes=0
Porcentage_Ray_Ant_Doa_votes=0
winner=0

# Read in the CSV file
with open(election_data_csv, newline='') as csv_file:
    # Split the data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')
    #The next () function returns the next item in the iterator
    header=next(csv_reader)
    
    # Read through each row of data after the header
    for row in csv_reader:
        
        # calculate the total votes
        total_votes += 1
        
        #calculate the number of votes for Charles Casper Stockham
        if row[2]== "Charles Casper Stockham":
            Char_Cas_Sto_votes += 1
            
        #calculate the number of votes for Diana DeGette
        if row[2]== "Diana DeGette":
            Dia_DeG_votes+= 1
            
        #calculate the number of votes for Raymon Anthony Doane
        if row[2]== "Raymon Anthony Doane":
            Ray_Ant_Doa_votes+= 1
           
    # calculate percentage of votes of Charles Casper Stockham
    Porcentage_Char_Cas_Sto_votes=(Char_Cas_Sto_votes/total_votes)*100
    
    # calculate percentage of votes of Diana DeGette
    Porcentage_Dia_DeG_votes=(Dia_DeG_votes/total_votes)*100
    
    # calculate percentage of votes of Raymon Anthony Doane
    Porcentage_Ray_Ant_Doa_votes=(Ray_Ant_Doa_votes/total_votes)*100
    
    #find the winner of the election based on popular vote
    if Char_Cas_Sto_votes>Dia_DeG_votes and Char_Cas_Sto_votes>Ray_Ant_Doa_votes:
        winner="Charles Casper Stockham"  
    elif Dia_DeG_votes>Char_Cas_Sto_votes and Dia_DeG_votes>Ray_Ant_Doa_votes:
        winner="Diana DeGette"
    else:
        winner="Raymon Anthony Doane"
    
#Reduce the number of decimal places to 3
Porcentage_Char_Cas_Sto_votes=round(Porcentage_Char_Cas_Sto_votes, 3)   
Porcentage_Dia_DeG_votes=round(Porcentage_Dia_DeG_votes,3)      
Porcentage_Ray_Ant_Doa_votes=round(Porcentage_Ray_Ant_Doa_votes,3)

# Output
output_information = (
    f"\nElection Results\n"
    f"\n-----------------------------\n"
    f"\nTotal Votes: {total_votes}\n"
    f"\n-----------------------------\n"
    f"\nCharles Casper Stockham: {Porcentage_Char_Cas_Sto_votes}% ({Char_Cas_Sto_votes})\n"
    f"\nDiana DeGette: {Porcentage_Dia_DeG_votes}% ({Dia_DeG_votes})\n"
    f"\nRaymon Anthony Doane: {Porcentage_Ray_Ant_Doa_votes}% ({Ray_Ant_Doa_votes})\n"
    f"\n-----------------------------\n"
    f"\nWinner: {winner} \n"
    f"\n-----------------------------\n"
    
)

print(output_information)

#export a text file with the results
with open("PyPoll/analysis/Analysis_Pypoll.txt","wt") as file:
    file.write(output_information)