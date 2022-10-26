# ADS: Ayman Habib, Sam Lubelsky, Daniel Liu
# Softdev pd02
# k17-18
# 2022-10-25
# time spent: 0.7 hr

import sqlite3   #enable control of an sqlite database
import csv

from csv_to_db import csv_to_db       #facilitate CSV I/O


DB_FILE="school.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

courses_header = "(name TEXT, age NUMERIC, id NUMERIC)"   # run SQL statement
students_header = "(name TEXT, age NUMERIC, id NUMERIC)"
csv_to_db(c, "courses.csv","courses",courses_header)
csv_to_db(c, "students.csv","students",students_header)

#==========================================================

db.commit() #save changes
db.close()  #close database


