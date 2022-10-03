"""
Jeff Chen
SoftDev
K06 - Randomly select a job with weighted percentages
2022-9-30
time spent: 45 min
DISCO: 
Built in CSV reader
del dict[key] deletes a key from dictionary
csvreader is not a list, it is a special python object called an iterable
that must be iterated through with a for loop
QCC:
what exactly is an iterable and can they be converted to lists?
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
def choose_job(jobs: dict):
    randomJob = random.random()*99.8
    #print(randomJob)
    chance = 0
    #print(randomJob, chance)
    for e in jobs:
        chance += jobs[e]
        if randomJob < chance:
            chosenJob = e
            break
    return chosenJob
def printJob(job):
    print("Chosen Job is " + job)
for _ in range(100):
    chosenJob = choose_job(jobs)
    printJob(chosenJob)
#additional tests
num_tests = 1_000_000
test_dict = {}
for _ in range(num_tests):
    job = choose_job(jobs)
    if job not in test_dict:
        test_dict[job] = 1
    else:
        test_dict[job] += 1
for num in test_dict:
    test_dict[num] /= num_tests
print(test_dict)



