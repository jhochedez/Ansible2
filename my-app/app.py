from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, {{  tower_user_name  }}!</p>"

@app.route("/tp")
def hello_2():
    return "<p>Hello, Ansible!</p>"

