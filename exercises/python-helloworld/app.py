from flask import Flask
import json


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World! Udacity course!"


@app.route("/metrics")
def show_metrics():
    return {"data": {"UserCount": 140, "UserCountActive": 23}}


@app.route("/status")
def show_status():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype="application/json",
    )
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0")
