from flask import Flask
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, NumberRange
from wtforms import StringField, IntegerField
import subprocess
import shlex

app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(validators=[InputRequired(), NumberRange(min=1, max=30)])


@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm()
    if form.validate_on_submit():
        code, timeout = form.code.data, form.timeout.data
        popen = shlex.split(f'prlimit --nproc=1:1 python -c "{code}"')
        process = subprocess.Popen(popen, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        try:
            output, error = process.communicate(timeout=timeout)
            return output.decode()
        except subprocess.TimeoutExpired:
            process.kill()
            return "Code execution exceeded the given timeout"
    else:
        return form.errors, 400


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
