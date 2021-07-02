#importing os module
import os
#import module to read csv files
import csv

csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

#opening csv file
with open (csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')

        #read header first
        csv_header = next(csvreader)

        #counting months
        months = 0

        #net amount of profit/loss
        net = 0

        #setting up variables
        firstrow = next(csvreader)
        value = int(firstrow[1])
        change = 0
        dates = []
        profits = []
        months += 1
        net += int(firstrow[1])

        for row in csvreader:
            #counting up months as rows go by
            months += 1
            #summing up profits/losses as rows go by
            net += int(row[1])

            #adding dates to a separate list
            dates.append(row[0])

            #recording change
            change = int(row[1]) - value
            profits.append(change)
            value = int(row[1])

#Looking at greatest increase in profits
maximum = max(profits)
maxindex = profits.index(maximum)
maxdate = dates[maxindex]

#doing same thing for greatest decrease
minimum = min(profits)
minindex = profits.index(minimum)
mindate = dates[minindex]

#calculating average change
average = sum(profits)/len(profits)

#Showing results
print("Financial Analysis")
print("----------------------------")      
print(f"Total Months: {str(months)}")
print(f"Total: ${str(net)}")
print(f"Average Change: ${str(round(average, 2))}")
print(f"Greatest Increase in Profits: {maxdate} ${str(maximum)}")
print(f"Greatest Decrease in Profits: {mindate} ${str(minimum)}")


#making and exporting a txt file with results
txtresults = os.path.join("PyBank", "Analysis", "results.txt")
with open(txtresults, 'w+') as txtfile:
     line1 = "Financial Analysis"
     line2 = "----------------------------"   
     line3 = str(f"Total Months: {str(months)}")
     line4 = str(f"Total: ${str(net)}")
     line5 = str(f"Average Change: ${str(round(average, 2))}")
     line6 = str(f"Greatest Increase in Profits: {maxdate} ${str(maximum)}")
     line7 = str(f"Greatest Decrease in Profits: {mindate} ${str(minimum)}")
     txtfile.write(f"{line1} \n {line2} \n {line3} \n {line4} \n {line5} \n {line6} \n {line7}")