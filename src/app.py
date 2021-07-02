import os
import sys
import pytest
from flask import Flask, request

app = Flask(__name__)


def get_message(count):
    if count < 0:
        raise RuntimeError("Unexpected negative digit count")
    if count == 0:
        return "Sure as snuff, there ain't no digits in that there string!"
    if count > 100:
        estimate = (count // 100) * 100
        interjection = 'Consarnit' if count % 2 == 0 else 'Tarnation'
        noun = 'heap' if count // 5 == 0 else 'mess'
        return f"{interjection}! That's a whole {noun} of digits! There must be at least {estimate} numbers in there!"
    return f"I reckon I see {count} digits."


@app.route("/")
def root():
    s = request.args.get("s")
    if s is None:
        return {"error": "Missing URL parameter 's'"}, 400
    count = sum(c.isdigit() for c in s)
    return {"count": count, "message": get_message(count)}


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    if os.getenv("ENV") == "test":
        sys.exit(pytest.main())
    else:
        debug = os.getenv("ENV") == "development"
        app.run(host="0.0.0.0", port=5000, debug=debug)
