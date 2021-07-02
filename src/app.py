import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    return "Hello"


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    debug = os.getenv("ENV") == "development"
    app.run(host="0.0.0.0", port=5000, debug=debug)
