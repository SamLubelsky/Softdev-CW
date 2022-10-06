

# your heading here

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
QCC:
0. Not too sure...
1. Base folder for Ubuntu.
2. It would print to a file in the route that was given, in this case "\". Maybe.
3. It would print the name of the folder it's in, in this case __main__.
4. The file will contain the return string, "No hablo queso!".
5. In java you can run non static functions by calling them with Object.function().
...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''