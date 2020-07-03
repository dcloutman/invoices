from flask import Flask, render_template, url_for

import os
import logging



from invoices.views.IndexView import IndexView
from invoices.views.InvoiceView import InvoiceView


sys_logger = logging.getLogger()

sys_logger.info("Loading invoice app.")

APP_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT =  os.path.join(APP_PATH, os.pardir)
STATIC_ROOT = os.path.join(os.curdir, "static")
TEMPLATE_ROOT = os.path.join(os.curdir, "templates")
app = Flask(__name__, template_folder=TEMPLATE_ROOT, static_folder=STATIC_ROOT)


IndexView.register(app)
InvoiceView.register(app)


if not 'FLASK_HOST' in os.environ:
    sys_logger.error("Critical environment variable 'FLASK_HOST' was not defined. Exiting.")
    sys.exit(1)
if not 'FLASK_PORT' in os.environ:
    sys_logger.info("Environment variable 'FLASK_PORT' was not set. Setting default value of 5000.")
    os.environ['FLASK_PORT'] = '5000'
if not 'FLASK_DEBUG' in os.environ:
    sys_logger.info("Environment variable 'FLASK_DEBUG' was not set. Setting default value of False.")
    os.environ['FLASK_DEBUG'] = '0'


config_was_loaded = app.config.from_envvar('APP_SETTINGS')

if False == config_was_loaded:
    sys_logger.error("Could not load configuration file.")
    exit()


if __name__ == '__main__':
    app.run(debug=bool(int(os.environ['FLASK_DEBUG'])), host=os.environ['FLASK_HOST'], port=int(os.environ['FLASK_PORT']))
