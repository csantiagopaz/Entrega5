from flask import Flask
import pandas
import pymongo

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(threaded=True, port=5000)