# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #creates flask instance with name __main__

@app.route("/") # routes to localhost
def hello_world():
    print(__name__) #print out __main__ in terminal
    return "No hablo queso!"  # display No Habl Queso on screen

app.run()  #run app on localhost
                
