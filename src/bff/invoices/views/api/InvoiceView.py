from flask import make_response, current_app, url_for, jsonify, request
from flask_classful import FlaskView, route
from os import environ
import json
import requests

class InvoiceView ():
    route_prefix = '/api'
    route_base = '/invoice/'

    #def before_request(self, name):
    #   pass

    def after_request(self, name, response):
        return response

    def index(self):
        html = render_template('invoice.jinja')
        return html, 200
