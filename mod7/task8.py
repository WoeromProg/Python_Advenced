import logging
import requests
from flask import Flask, request
from logging_config_task4_5 import dict_config
from logging import config, handlers

app = Flask(__name__)


logger = logging.getLogger('httpLogger')
logging.config.dictConfig(dict_config)


@app.route('/logs/')
def get_logs():
    with open('utils.log', 'r') as log_file:
        data = log_file.read()
        data = data.replace('\n', '</br>')
    return data


@app.route('/logs/', methods=['POST'])
def post_log():
    log_data = request.json
    service_name = log_data.pop("service")

    try:
        level_str = log_data['level']
        level_num = getattr(logging, level_str.upper())

        logger.log(level_num, f"{service_name}: {log_data['message']}", extra=log_data)
        return "Success"

    except (ValueError, KeyError) as e:
        logger.error(f"Failed to log: {e}")
        return f"Failed: {e}", 400

if __name__ == '__main__':
    app.run(debug=True)