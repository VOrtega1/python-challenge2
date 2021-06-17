
"""
Created on Fri Apr  9 04:07:38 2021

@author: veronica o
"""
import csv
import os
 
# pull csv file
budgetcsv = os.path.join ('Resources','budget_data.csv')

# data placeholder
months = []
net_total = []
 
with open (budgetcsv, newline = "") as csvfile:
    readcsv = csv.reader(csvfile, delimiter = ',')
 
    csv_header = next(csvfile)
     
#put the data into lists
    for row in readcsv:
        months.append(row[0])
        net_total.append(int(row[1]))
         
#month count
    month_count = len(months)
     
#loop variables
    x = 1
    y = 0
     
#change placeholder
    chng_avg = (net_total[1]-net_total[0])
     
#placeholder changes 
    changes = []
     
# create list with loop for month to month calculations
    for month in range(month_count-1):
        chng_avg = (net_total[x] - net_total[y])
        changes.append(int(chng_avg))
        x+=1
        y+=1
         
     
 #Calcuate the average monthly change and round it    
    avg_month = round(sum(changes)/(month_count -1),2)
 
    #find min & max 
    chg_min = min(changes)
    chg_max = max(changes)
 
    #rtrn index for list positions
    minChng = changes.index(chg_min)
    maxChng = changes.index(chg_max)
     
    #find min & max by month
    minChng_month = months[minChng + 1]
    maxChng_month = months[maxChng + 1]
   
 
#Print the values to console
 
print("Financial Analysis")
print("----------------------------")
print(f"Months: {len(months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Monthly Change: {avg_month}")
print(f"Greatest Increase in Profits: {maxChng_month} (${chg_max})")
print(f"Greatest Decrease in Profits: {minChng_month} (${minChng})")
 
#Write text file output
final_analysis = open("Financial_Analysis.txt","w")
 
final_analysis.write("Financial Analysis\n")
final_analysis.write("-------------------\n")
final_analysis.write(f"Months: {len(months)}\n")
final_analysis.write(f"Total: ${sum(net_total)}\n")
final_analysis.write(f"Average Monthly Change: {avg_month}\n")
final_analysis.write(f"Greatest Increase in Profits: {maxChng_month} (${maxChng})\n")
final_analysis.write(f"Greatest Decrease in Profits: {minChng_month} (${minChng})\n")
 
  
final_analysis.close() 