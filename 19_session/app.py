# ADS: Ayman Habib, Sam Lubelsky, Daniel Liu
# Softdev pd02
# k12
# 2022-10-17
# time spent: 0.3 hr

from flask import Flask             #facilitate flask webserving
from flask import render_template, make_response   #facilitate jinja templating
from flask import request           #facilitate form submission
import os 

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)
#os.urandom(32)
#session[key] = value
#session.pop(key)
username = "ads"
password = "admin"
@app.route('/', methods=['GET','POST'])
def disp_loginpage():
    return render_template('login.html')


@app.route("/response", methods=['GET', 'POST'])
def authenticate():
    print("COOKIE INFO")
    print(request.cookies.get("username"))
    print(request.cookie.get("password"))
    userIn = request.form.get('username')
    passIn = request.form.get('password')
    print(request.cookies.get("username"))
    if(request.form.get("username") != username):
        return "wrong username"
    elif request.form.get("password") != password:
        return "wrong password"
    else:
        resp = make_response("welcome valued user!")
        resp.set_cookie('username', userIn)
        return resp


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
