import os
import sys
import pytest
import subprocess
from flask import Flask, request

os.environ.setdefault("REDIS_URL", "redis://localhost:6379/0")

app = Flask(__name__)


def get_message(count):
    if count < 0:
        raise RuntimeError("Unexpected negative digit count")
    if count == 0:
        return "Sure as snuff, there ain't no digits in that there string!"
    if count > 100:
        estimate = (count // 100) * 100
        interjection = "Consarnit" if count % 2 == 0 else "Tarnation"
        noun = "heap" if count // 5 == 0 else "mess"
        return f"{interjection}! That's a whole {noun} of digits! There must be at least {estimate} numbers in there!"
    return f"I reckon I see {count} digits."


@app.route("/")
def root():
    s = request.args.get("s")
    if s is None:
        return {"error": "Missing URL parameter 's'"}, 400
    count = sum(c.isdigit() for c in s)
    return {"count": count, "message": get_message(count)}


@app.route("/cowsay")
def cowsay():
    s = request.args.get("s")
    if s is None:
        return {"error": "Missing URL parameter 's'"}, 400

    cowsay_args = ["cowsay", s]
    cowsay_kwargs = {"stdout": subprocess.PIPE, "stderr": subprocess.STDOUT}
    process = subprocess.Popen(cowsay_args, **cowsay_kwargs)
    output, _ = process.communicate()
    return output


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    if os.getenv("ENV") == "test":
        test_artifacts_path = os.getenv("TEST_ARTIFACTS_PATH")
        pytest_args = (
            [f"--junitxml={test_artifacts_path}/test-results.xml"]
            if test_artifacts_path
            else []
        )
        sys.exit(pytest.main(pytest_args))
    else:
        debug = os.getenv("ENV") == "development"
        app.run(host="0.0.0.0", port=5000, debug=debug)
