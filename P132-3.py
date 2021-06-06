import csv

rows = [["Top Gun","Risky Business","Minority Report"],["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open("133-3.csv","w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
