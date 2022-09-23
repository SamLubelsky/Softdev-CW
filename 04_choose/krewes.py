
import random
'''
Julia Lee
SoftDev
K04 -- choose
2022-09-23
time spent: class time (2*41 = 82 mins)
DISCO:
Import random
random.random * range
type casting: int() list()
krewes.keys() doesn't automatically return the list of keys, so you have to typecast it into a list.
QCC:
What kind of data type is krewes.keys()? It's not a list but it can be typecasted to a list of the keys.
Why are some of krewes names capitalized and some not???
We decided to make this a function, but what was the intended final product? 
OPS SUMMARY:
We first randomized the index of the key of krewes by utilizing random(). We multiplied random() by the how many keys
there are before typcasting it to an int with int(). We multiplied by the length of the list of krewes.key() before typecasting because otherwise we would only be given the value 0.
The actual key value was then saved in key using the keyindex.
We followed a similar process for finding the final value.
In order to make the code more flexible, we used the length of krewes and krewes.keys() instead of inserting specific values.
'''
def choose():
    krewes = {2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"],
              7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
              8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "wanying"]}
    keyindex = int(random.random()*len(list(krewes.keys())))
    key = list(krewes.keys())[keyindex]
    valindex = int(random.random()*len(krewes[key]))
    return krewes[key][valindex]

for i in range(100):
    print(choose())