#Need to import flask class which will allow use to create a WSGI
from flask import Flask

app = Flask(__name__)

@app.route("/")
def automation_bot():
    return "<p>Automation Bot!</p>"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)