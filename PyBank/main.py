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

        for row in csvreader:
            months += 1
            net += int(row[1])



        average = net/months

        
print(months)
print(net)
print(average)





#making and exporting a txt file with results
#txtresults = os.path.join("Analysis", "results.txt")
#with open(txtresults, 'w+') as txtfile:
#      txtfile.write("Financial Analysis \n ---------------------------- \n" + ) 