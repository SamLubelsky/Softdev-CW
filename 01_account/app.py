# Faiza Huda
# SoftDev
# Oct 2022

from functools import total_ordering
from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
import hashlib
#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
totally_secure = {}


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. 
TASK: Predict which...
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests.
Process results.

PROTIP: Insert your own in-line comments
    wherever they will help
    your future self and/or current teammates
    understand what is going on.
'''

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #### This breaks code bc there is no username key or any key for that fact
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    ####
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'login.html' )


@app.route("/auth" , methods= ['GET','POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    if request.method == "POST":
        print("***DIAG: request.args ***") # ImmutableMultiDict([('username', 'looloo'), ('sub1', 'Submit')])
        #print(request.args) #Seems to output nothing for POST
        print(request.form['username']) # This works however
        username, password = request.form['username'], request.form['password']

        if username in totally_secure:
            print("making hash")
            hash = hashlib.sha256(password.encode()).hexdigest()
            print(hash, totally_secure[username])
            if totally_secure[username] == hash:
                return "congrates you made it"
        return "wrong password or username try again :("
    else: 
        # It seems that when trying this method with POST form request it breaks
        print("***DIAG: request.args['username']  ***")
        print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return "Waaaa hooo HAAAH"  #response to a form submission

@app.route("/create_acc", methods= ['GET','POST'])
def create():
    print("HELOO???")
    return render_template( 'account.html')

@app.route("/adding", methods= ['GET','POST'])
def update():
    password = request.form['password']
    hash = hashlib.sha256(password.encode()).hexdigest()
    totally_secure[request.form['username']] = hash
    return disp_loginpage()


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
