#importing os module
import os
#import module to read csv files
import csv

csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

#opening csv file
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')    

        #read header first
        csv_header = next(csvreader)

        #making a list for candidates
        candidates = []

        #making list for percentage
        percentage = []

        total = 0

        #making list for each candidate votes
        candivotes = []

        for row in csvreader:
            total += 1

            #adding candidate in list and summing votes per candidate
            if row[2] not in candidates:
                candidates.append(row[2])
                index = candidates.index(row[2])
                candivotes.append(1)
            else:
                index = candidates.index(row[2])
                candivotes[index] += 1
        
        #calculating percentage 
        for vote in candivotes:
            percent = (vote/total) * 100
            percentage.append(percent)
        roundpercentage = ['%.3f' % elem for elem in percentage]

        #calculating winner
        maximum = max(candivotes)
        index = candivotes.index(maximum)
        winner = candidates[index]

print("Election Results")
print("-------------------------------")
print(f"Total Votes: {str(total)}")
print("-------------------------------")
for candidate in range(len(candidates)):
    print(f"{candidates[candidate]}: {str(roundpercentage[candidate])}% ({str(candivotes[candidate])})")
print("-------------------------------")
print(f"Winner: {winner}")
print("-------------------------------")

#export text file
txtresults = os.path.join("PyPoll", "Analysis", "results.txt")
with open(txtresults, 'w+') as txtfile:
    line1 = "Election Results"
    line2 = "-------------------------------"
    line3 = str(f"Total Votes: {str(total)}")
    line4 = "-------------------------------"
    txtfile.write(f"{line1} \n {line2} \n {line3} \n {line4} \n")
    for candidate in range(len(candidates)):
        lines = str(f"{candidates[candidate]}: {str(roundpercentage[candidate])}% ({str(candivotes[candidate])})")
        txtfile.write(f"{lines} \n")
    line9 = "-------------------------------"
    line10 = str(f"Winner: {winner}")
    line11 = "------------------------------"
    txtfile.write(f"{line9} \n {line10} \n {line11}")
