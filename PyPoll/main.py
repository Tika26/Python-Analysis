import csv
data = csv.reader(open('Resources/election_data.csv'))
my_report = open('Analysis/Election_Report.txt', 'w')

next(data)

votes = 0
candidates_dict = {}
winner = ['',0]

for row in data:

    votes += 1
    candidate_name=row[2]

    if candidate_name not in candidates_dict.keys():
        candidates_dict[candidate_name] = 0

    candidates_dict[candidate_name] += 1 

output = f'''
Election Results
-------------------------
Total Votes: {votes:,}
-------------------------
'''
    
for candidate_name in candidates_dict.keys():
    output += f'{candidate_name}: {candidates_dict[candidate_name]/votes*100 :.3f}% ({candidates_dict[candidate_name]:,})\n'

    if candidates_dict[candidate_name] > winner[1]:
        winner[0] = candidate_name
        winner[1] = candidates_dict[candidate_name]


output += f' -------------------------\nWinner: {winner[0]}\n-------------------------'

print(output)
my_report.write(output)