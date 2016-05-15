from flask import Flask
import os

port = os.environ.get("PORT", 1337)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/hello")
def hello():
    return "World"

@app.route("/worlds")
def worlds():
    return "PLUTO"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=port)
