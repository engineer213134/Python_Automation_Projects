#This will be creating API's with python using the flask libary in python
#Flask is a micro web framework for python and can be used to create web applications from scratch

#Import the flask module
from flask import Flask

#To invoke instance of the flask class
app = Flask(__name__)

#Using a decorator in pythom
@app.route("/")
def automation_bot():
    return "<p>Automation Bot!</p>"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)












