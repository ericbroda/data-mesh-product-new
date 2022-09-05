from flask import Flask


app = Flask(__name__)


@app.route('/observe')
def observe():
    return "hello observe"

@app.route('/discover')
def discover():
    return "hello discover"



HOST = "0.0.0.0"
PORT = 8080

if __name__ == '__main__':
    try:
        app.run(host=HOST, port=PORT)
    finally:
        print("LOG dododododododo")
