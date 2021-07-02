#importing os module
import os
#import module to read csv files
import csv

csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

#opening csv file
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')    
        