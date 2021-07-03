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
