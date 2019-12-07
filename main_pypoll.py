import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join("Resources", "election_data.csv")

unique_names = []
votes = {}

votecount = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader: 
        votecount += 1
        name = row[2]
        if name not in unique_names: 
            unique_names.append(name)
    
        if name not in votes:
            votes[name] = 1
        else:
            votes[name] = votes[name] + 1                                     

print("Election Results")
print("-----------------------")
print("Total Votes" + " " + str(votecount))
print("--------------------------")
for name in votes:
    print(name, round(votes[name] / votecount * 100, 2) ,"%", votes[name])
print("--------------------------")
winner_name = ""
winner_votes = 0
for name in votes:
     if winner_votes < votes[name]:
        winner_name = name
        winner_votes = votes[name]
print("Winner:" + winner_name)
print("--------------------------")

os.chdir(os.path.dirname(os.path.abspath(__file__)))
output_path = os.path.join("Output", "pypoll.csv")

with open(output_path, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-----------------------"])
    csvwriter.writerow(["Total Votes" + " " + str(votecount)])
    csvwriter.writerow(["--------------------------"])
    for name in votes:
        csvwriter.writerow([name, round(votes[name] / votecount * 100, 2), "%", votes[name]])
    csvwriter.writerow(["--------------------------"])
    csvwriter.writerow(["Winner:" + winner_name])
    csvwriter.writerow(["--------------------------"])
