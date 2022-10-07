import csv
import random
from flask import Flask
import random
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
def job_to_url(job_name, chance = 0.05):
    randNum = random.random();
    if randNum < chance:
        return "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    else:
        base_url = "https://www.usajobs.gov/Search/Results?k="
        job_url = job_name.replace(',', '').replace(' ', '%20')
        return base_url + job_url

#display page
@app.route("/")
def page():
    randomJob = choose_job(jobs) 
    jobs_string = ',\n'.join(list(jobs)) #put newlines between jobs
    full_urls = []
    jobs_list = list(jobs)
    for i in range(len(jobs)):
        s = f'<a href ={job_to_url(jobs_list[i], 0.25)}> {jobs_list[i]}</a>'
        full_urls.append(s)
    full_urls = '\n'.join(full_urls)
    #print("hello")
    s = f'''<!doctype html> <head> DTurt: Sam, Faiza, Hui
    Softdev Period
    </head><body>
    <a href = "{job_to_url(randomJob, 0)}">
    {randomJob}
    </a>

    {full_urls}
    </body>
    '''
    s = '<br>'.join(s.split("\n")) #replace newlines with <br> for html formatting
    return s

#print(job_to_url("farmer and gardenders"))
app.run()