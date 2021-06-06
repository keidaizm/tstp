import csv

with open("test2.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["1","two","three"])
    w.writerow(["4","five","six"])
          
