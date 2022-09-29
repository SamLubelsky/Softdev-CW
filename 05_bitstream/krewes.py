'''
Samuel Lubelsky
Softdev
K05 - Read, parse, and display contents of txt file containing pds, dev names, and ducky names
2022-09-29
time spent: 
DISCO:
QCC:

'''
import random
with open('krewes.txt','r') as f:
    inputString = f.read()
devos = inputString.strip('\n').split("@@@")
for i in range(len(devos)):
    devos[i] = devos[i].split("$$$")
randomDevo = random.choice(devos)
devoPeriod, devoName, duckName = randomDevo[0], randomDevo[1], randomDevo[2]
print(f'{devoName} is in period {devoPeriod} and their ducky\'s name is {duckName}')

