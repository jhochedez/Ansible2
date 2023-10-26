from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, {}!</p>".format(tower_user_name)

@app.route("/tp")
def hello_2():
    return "<p>Hello, Ansible!</p>"

