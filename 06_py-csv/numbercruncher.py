"""
Jeff Chen
SoftDev
K06 - Randomly select a job with weighted percentages
2022-9-30
time spent: 45 min
DISCO: 
Built in CSV reader
QCC:
"""

jobs = {}

import csv
import random

##opens and prints out content of csv
with open("./occupations.csv", 'r') as file:
  csvreader = csv.reader(file)
  line_count = 0
  for row in csvreader:
      if line_count != 0:
          ##print(row)
          jobs[row[0]] = float(row[1])
      line_count = line_count + 1
  del jobs["Total"]

  ##for e in jobs:
  ##    print(e)

randomJob = random.random()*99.8
print(randomJob)

chance = jobs[list(jobs)[0]]
for e in jobs:
    if randomJob < chance:
        print(e)
        break
    chance = chance + jobs[e]