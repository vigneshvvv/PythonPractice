from flask import Flask, jsonify
from mySql import mySqlConnect

app = Flask(__name__)

@app.route('/home', methods = ['GET'])
def getValueFromServer():
    data = mySqlConnect()
    return jsonify(data)


if __name__ == '__main__':
    app.run(port= 8080)
