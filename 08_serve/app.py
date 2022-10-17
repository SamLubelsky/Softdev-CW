import csv
import random
from flask import Flask

jobs = {}
app = Flask(__name__)

##opens and prints out content of csv
with open("./occupations.csv", 'r') as file:
  csvreader = csv.reader(file)
  line_count = 0
  for row in csvreader:
      if line_count != 0:  #exclude first row of csv
          ##print(row)
          jobs[row[0]] = float(row[1]) #first value of csv line is key, second value is value
      line_count = line_count + 1
  del jobs["Total"]
  ##for e in jobs:
  ##    print(e)

#print random job from jobs dict
def choose_job(jobs: dict):
    return random.choices(list(jobs), weights = list(jobs.values()))[0] #builtin weighted choice function
    
#display page
@app.route("/")
def page():
    randomJob = choose_job(jobs)
    jobsString = ',\n'.join(list(jobs)) #put newlines between jobs
    s = f'''
    <!doctype html>
    <head>
    DTurt: Sam, Faiza, Hui
    Softdev Period 2
    k08
    2022-10-06
    Time Spent: 0.5
    </head>
    <body>
    {randomJob}

    {jobsString}
    </body>
    '''
    s = '<br>'.join(s.split("\n")) #replace newlines with <br> for html formatting
    return s

app.run()