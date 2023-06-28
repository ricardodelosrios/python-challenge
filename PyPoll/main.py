import os
import csv

# Ruta del archivo a cargar
election_data_csv = "PyPoll\Resources\election_data.csv"

# Declarar variables
total_votes = 0
Char_Cas_Sto_votes=0
Dia_DeG_votes=0
Ray_Ant_Doa_votes=0
Porcentage_Char_Cas_Sto_votes=0
Porcentage_Dia_DeG_votes=0
Porcentage_Ray_Ant_Doa_votes=0
winner_Char=0
winner_Dia=0
winner_Ray=0
winner=0


# CSV reader
with open(election_data_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    
    # Loop to count total votes and # of votes for each candidate
    for row in csv_reader:
        # Calcular el total de votos
        total_votes += 1
        #create variables
        
        #Number of votes for Charles Casper Stockham
        
        if row[2]== "Charles Casper Stockham":
            Char_Cas_Sto_votes += 1
            
        
        #Number of votes for Diana DeGette
        
        if row[2]== "Diana DeGette":
        
            Dia_DeG_votes+= 1
            
        
        #Number of votes for Raymon Anthony Doane
        
        if row[2]== "Raymon Anthony Doane":
        
            Ray_Ant_Doa_votes+= 1
           
    # calculate percentage of vote of Charles Casper Stockham
    
    Porcentage_Char_Cas_Sto_votes=(Char_Cas_Sto_votes/total_votes)*100
    
    # calculate percentage of vote of Diana DeGette
    
    Porcentage_Dia_DeG_votes=(Dia_DeG_votes/total_votes)*100
    
    # calculate percentage of vote of Raymon Anthony Doane
    
    Porcentage_Ray_Ant_Doa_votes=(Ray_Ant_Doa_votes/total_votes)*100
    
    if Char_Cas_Sto_votes>Dia_DeG_votes and Char_Cas_Sto_votes>Ray_Ant_Doa_votes:
        winner="Charles Casper Stockham"  
    elif Dia_DeG_votes>Char_Cas_Sto_votes and Dia_DeG_votes>Ray_Ant_Doa_votes:
        winner="Diana DeGette"
    else:
        winner="Raymon Anthony Doane"
    
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

with open("PyPoll/analysis/Analysis_Pypoll.txt","wt") as file:
    file.write(output_information)