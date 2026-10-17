from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

@app.route("/testroute")
def testing_route():
    return "<h1>Route Testing!</h1>"