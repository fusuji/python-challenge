#importing os module
import os
#import module to read csv files
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

#opening csv file
with open (csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')

        #read header first
        csv_header = next(csvreader)
        