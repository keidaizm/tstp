import csv

rows = [["トップガン","リスキービジネス","マイノリティリポート"],["タイタニック", "ザ・レヴェナント", "インセプチョン"], ["トレーニングデイ", "炎の人", "フライト"]]

#with open("133-3jp.csv","w",encoding="utf-8") as f:
with open("133-3jp.csv","w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
