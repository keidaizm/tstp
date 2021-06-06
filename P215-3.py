import re


t = "The ghost that says boo haunts the loo"

results = re.findall(".oo", t)

print(results)
