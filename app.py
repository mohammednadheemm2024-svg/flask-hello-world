from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from PaaS Lab! Student: M.MOHAMMED NADHEEM, Roll No: 24MID0030'
