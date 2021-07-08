from flask import Flask
import json
import logging


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World! Udacity course!"


@app.route("/metrics")
def show_metrics():
    app.logger.info("Show metrics")
    return {"data": {"UserCount": 140, "UserCountActive": 23}}


@app.route("/status")
def show_status():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype="application/json",
    )
    app.logger.info("Show status")
    return response


if __name__ == "__main__":
    logging.basicConfig(filename="app.log", level=logging.DEBUG)
    app.run(host="0.0.0.0")
