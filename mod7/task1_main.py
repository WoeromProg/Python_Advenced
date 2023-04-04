import logging
from flask import Flask
from task1_http_utils import get_ip_address
from task1_subprocess_utils import get_kernel_version


logging.basicConfig(level='DEBUG')
logger = logging.getLogger('main')

app = Flask(__name__)


@app.route('/get_system_info')
def get_system_info():
    logger.info('Start working')
    ip = get_ip_address
    kernel = get_kernel_version()
    return "<p>{}</p><p>{}</p>".format(ip, kernel)


if __name__ == '__main__':
    app.run(debug=True)