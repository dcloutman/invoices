from flask import make_response, render_template, current_app, url_for, jsonify, request
from flask_classful import FlaskView, route
from os import environ

from invoices.models.Invoice import Invoice
from invoices.models.InvoiceItem import InvoiceItem

class InvoiceView (FlaskView):
    route_prefix = ''
    route_base = '/invoice/'

    #def before_request(self, name):
    #   pass

    def after_request(self, name, response):
        return response

    def index(self, id):
        if '0001' == id:
            html = render_template('invoice.jinja')
            return html, 200
        else:
            return "Not found", 404

