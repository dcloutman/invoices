from flask import make_response, current_app, url_for, jsonify, request
from flask_classful import FlaskView, route
from os import environ
import json
import requests

class InvoiceItemView ():
    route_prefix = '/api'
    route_base = '/invoice-item/'

    def after_request(self, name, response):
        return response

    def index(self, id):
        if '0001' == id:
            html = render_template('invoice.jinja')
            return html, 200
        else:
            return "Not found", 404
