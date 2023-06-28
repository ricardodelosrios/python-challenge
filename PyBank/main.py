import os
import csv
# Ruta del archivo a cargar
budget_data_csv="PyBank/Resources/budget_data.csv"
#crear diccionario meses
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

#declarar la variable para el total del presupuesto
total=0
#declarar min-max
decrease=0
increase=0
decrease_date=""
increase_date=""
total_changes=0
actual_budget=0
#flat variable
flat=False
#abrir el archivo 
with open(budget_data_csv) as csv_budget_data:
    # leyendo el archivo en formato csv
    csv_reader=csv.reader(csv_budget_data, delimiter=",")
    # next para saltar la cabecera del csv
    next(csv_reader)
    # Read through each row of data after the header
    
    for row in csv_reader:
        #crear la variable date
        date=row[0]
        #crear la variable profit_losses
        Profit_Losses=int(row[1])
        #definir el numero de caracteres de la fecha a leer
        date_t=date[0:3]
        #cada vez de apariciones del mes va a sumar 1
        months[date_t]=months[date_t]+1
        total=total+Profit_Losses
        
        changes_profit_losses=Profit_Losses-actual_budget
        #para cada uno de los cambios verificar max y min respecto a actual
        if changes_profit_losses > increase:
            increase=changes_profit_losses
            increase_date=date
        if changes_profit_losses < decrease:
            decrease=changes_profit_losses
            decrease_date=date
        actual_budget=Profit_Losses
        #excluir en el cambio de presupuesto la primera fila por una bandera
        if(flat):
            total_changes=total_changes+changes_profit_losses
        else:
            flat=True
        #extraer los valores del diccionario
    total_months=months.values()
    # sumar los meses en la variable total meses 
    total_months=(sum(total_months))
    average=total_changes/(total_months-1)
    average=round(average,2)
    print("Financial Analysis\n----------------------------")
    print("Total Months: {}".format(total_months))
    print("Average Change: ${}".format(average))
    print("Total: ${}".format(total))
    print("Greatest Increase in Profits: {} (${})".format(increase_date, increase))
    print("Greatest Decrease in Profits: {} (${})".format(decrease_date, decrease))
    

    




   

