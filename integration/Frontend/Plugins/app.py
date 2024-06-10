from flask import Flask, request

from main import resp

app = Flask(__name__)

@app.route('/example')
def example():
    # assuming the data sent is JSON
    return resp()

if __name__ == '__main__':
    app.run(debug=True)
