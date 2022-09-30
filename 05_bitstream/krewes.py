"""
Jeff Chen, Samuel Lubelsky
SoftDev
K05 - Read, parse, and display contents of txt files containing pds, dev names, and ducky names.
2022-9-29
time spent: 45mins
DISCO: 
Use "with open() as f" with filename, mode to open a file for parsing.
inputstring = file.read() to turn input into a string
file.read() returns contents of file
strip removes specified string from front and back of string
QCC:
Why does my code still have a /n at the end even though I used strip???
What are the modes for open()?
"""

import random
with open('krewes.txt', 'r') as f:
    inputString = f.read()
devos = inputString.strip('/n').split("@@@")
for i in range(len(devos)):
    devos[i] = devos[i].strip('/n').split("$$$")
randomDevo = random.choice(devos)
devoPeriod, devoName, duckName = randomDevo[0], randomDevo[1], randomDevo[2]
print(f'{devoName} is in period {devoPeriod} and their ducky\'s name is {duckName}')



