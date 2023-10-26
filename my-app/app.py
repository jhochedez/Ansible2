from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/tp")
def hello_2():
    return "<p>Hello, Ansible!</p>"

