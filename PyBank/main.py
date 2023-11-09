import csv
data = csv.DictReader(open('Resources/budget_data.csv'))
my_report = open('Analysis/Budget_Report.txt', 'w')

months = 0
total = 0
total_CH = 0
pre_rev = 0
inc = ['',0]
dec = ['', 0]

for row in data:
    months += 1

    rev = int(row['Profit/Losses'])
    total += rev

    change = rev - pre_rev
    if pre_rev == 0:
        change = 0

    total_CH += change

    if change > inc[1]:
        inc[0] = row['Date']
        inc[1] = change

    if change < dec[1]:
        dec[0] = row['Date']
        dec[1] = change
    

    pre_rev = rev

output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total}
Average Change: ${total_CH/(months-1):,.2f}
Greatest Increase in Profits: {inc[0]} (${inc[1]:,}) 
Greatest Decrease in Profits: {dec[0]} (${dec[1]:,})
'''

print(output)
my_report.write(output)