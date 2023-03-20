import shlex
import string
import subprocess
from typing import List
from flask import Flask, request

app = Flask(__name__)

@app.route("/uptime", methods=['GET'])
def _uptime():
    arg = request.args.get("arg")
    args_cleaned = shlex.quote(arg)
    result = subprocess.run(args_cleaned, capture_output=True)

    if result.returncode != 0:
        return "Error", 500
    output = result.stdout.decode()
    return string.Template(f"<pre>${output}</pre>").substitute(output=output)


@app.route("/ps", methods=["GET"])
def _ps():
    args: List[str] = request.args.getlist("arg")
    args_cleaned = [shlex.quote(s) for s in args]
    command_str = f"ps {' '.join(args_cleaned)}"
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)

    if result.returncode != 0:
        return "Error", 500
    output = result.stdout.decode()
    return  string.Template(f"<pre>${output}</pre>").substitute(output=output)


if __name__ == "__main__":
    app.run(debug=True)