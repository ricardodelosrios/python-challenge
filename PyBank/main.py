#Import from operative system an csv file
import os
import csv

# Path to collect data from the Resources folder
budget_data_csv="PyBank/Resources/budget_data.csv"

#directory of months
months={
    "Jan":0,
    "Feb":0,
    "Mar":0,
    "Apr":0,
    "May":0,
    "Jun":0,
    "Jul":0,
    "Aug":0,
    "Sep":0,
    "Oct":0,
    "Nov":0,
    "Dec":0
}

#declare the variables
total=0
decrease=0
increase=0
decrease_date=""
increase_date=""
total_changes=0
actual_budget=0
#flat variable
flat=False
#Read in the CSV file 
with open(budget_data_csv) as csv_budget_data:
    # Split the data on commas
    csv_reader=csv.reader(csv_budget_data, delimiter=",")
    # The next () function returns the next item in the iterator
    header=next(csv_reader)
    
    # Read through each row of data after the header
    
    for row in csv_reader:
        #create the date variable
        date=row[0]
        #create the profit_losses variable
        Profit_Losses=int(row[1])
        #define the number of characters of the date to read
        date_t=date[0:3]
        #calculate the number of occurrences of the months and add 1
        months[date_t]=months[date_t]+1
        #Calculate the net total amount of "Profit/Losses" over the entire period
        total=total+Profit_Losses
        
        changes_profit_losses=Profit_Losses-actual_budget
        #check max and min (date and profit losses)
        if changes_profit_losses > increase:
            increase=changes_profit_losses
            increase_date=date
        if changes_profit_losses < decrease:
            decrease=changes_profit_losses
            decrease_date=date
        actual_budget=Profit_Losses
        #remove the first row by a flag
        if(flat):
            total_changes=total_changes+changes_profit_losses
        else:
            flat=True
        #extract values from dictionary
    total_months=months.values()
    # add the months in the variable total months
    total_months=(sum(total_months))
    #calculate the average
    average=total_changes/(total_months-1)
    average=round(average,2)
    
    # Output
    
    output_information = (
    f"\nFinancial Analysis\n"
    f"\n-----------------------------\n"
    f"\nTotal Months: {total_months}\n"
    f"\nTotal: $ {total}\n"
    f"\nAverage Change: ${average}%\n"
    f"\nGreatest Increase in Profits: {increase_date} ({increase})\n"
    f"\nGreatest Decrease in Profits: {decrease_date} ({decrease})\n"
    
)

print(output_information)

#export a text file with the results
with open("PyBank/analysis/Analysis_PyBank.txt","wt") as file:
    file.write(output_information)
    

    




   

