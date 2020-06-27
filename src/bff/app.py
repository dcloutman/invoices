from flask import Flask, render_template
from invoices.models.Invoice import Invoice
from invoices.models.InvoiceItem import InvoiceItem


import os
import logging

# from lib.citadel.diff.views.DiffView import DiffView
# from lib.citadel.diff.views.JobDataView import JobDataView
# from lib.citadel.diff.views.GetDiffReportOidView import GetDiffReportOidView
# from lib.citadel.diff.views.GetDiffReportView import GetDiffReportView

print("Loading invoice app.")

APP_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT =  os.path.join(APP_PATH, os.pardir)
STATIC_ROOT = os.path.join(os.curdir, "static")

app = Flask(__name__, template_folder=os.path.join(PROJECT_ROOT, "ui/src/jinja2_templates"), static_folder=STATIC_ROOT)
sys_logger = logging.getLogger()

if not 'FLASK_PORT' in os.environ:
    sys_logger.info("Environment variable 'FLASK_PORT' was not set. Setting default value of 5000.")
    os.environ['FLASK_PORT'] = '5000'
if not 'FLASK_DEBUG' in os.environ:
    sys_logger.info("Environment variable 'FLASK_DEBUG' was not set. Setting default value of False.")
    os.environ['FLASK_DEBUG'] = '0'


if __name__ == '__main__':
    app.run(debug=bool(int(os.environ['FLASK_DEBUG'])), host=os.environ['FLASK_HOST'], port=int(os.environ['FLASK_PORT']))
