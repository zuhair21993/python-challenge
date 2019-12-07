import os
import csv 

#defining path for the file to read
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
#setting list to collect dates

#setting variables for calculation
    
    months = 0
    total_profits = 0
    prev_month_pl = 0
    pl_diff_total = 0
    average_monthly_change = 0
    greatest_profits_increase = 0
    increased_profit_date = 0
    greatest_profits_decrease = 0
    decreased_profit_date = 0
    
    for row in csvreader:
        
#month count calculation
        months += 1
        curr_month_pl = int(row[1])
        
        #total profit calculation
        total_profits += curr_month_pl
#month > 1 as first month will not have a difference (no past comparison against)
        if months > 1:
            pl_diff = curr_month_pl - prev_month_pl
            
            pl_diff_total += pl_diff
#average of monthly change, returning one month back as first month will have no difference
            average_monthly_change = pl_diff_total / (months - 1)

            if pl_diff > greatest_profits_increase:
                greatest_profits_increase = pl_diff                
                increased_profit_date = row[0]

            if  pl_diff < greatest_profits_decrease:
                greatest_profits_decrease = pl_diff
                decreased_profit_date = row[0]       
        prev_month_pl = curr_month_pl
                
print("Financial Analysis")
print("--------------------------")
print("Total Months:" + " " + str(months))
print("Total:" + " " + "$" + str(total_profits))
print("Average change:" + " " +  "$" + str(average_monthly_change))
print("Greatest increase in profits:" + " " + str(increased_profit_date) + " " + "$" + str(greatest_profits_increase))
print("Greatest decrease in profits:" + " " + str(decreased_profit_date) + " " + "$" + str(greatest_profits_decrease))

os.chdir(os.path.dirname(os.path.abspath(__file__)))
output_path = os.path.join("Output", "pybank.csv")

with open(output_path, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["--------------------------"])
    csvwriter.writerow(["Total Months:" + " " + str(months)])
    csvwriter.writerow(["Total:" + " " + "$" + str(total_profits)])
    csvwriter.writerow(["Average change:" + " " +  "$" + str(average_monthly_change)])
    csvwriter.writerow(["Greatest increase in profits:" + " " +  "$" + str(greatest_profits_increase)])
    csvwriter.writerow(["Greatest decrease in profits:" + " " +  "$" + str(greatest_profits_decrease)])
