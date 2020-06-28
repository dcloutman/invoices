from flask import make_response, render_template, current_app, url_for, jsonify, request
from flask_classful import FlaskView, route
from os import environ

class IndexView (FlaskView):
    route_prefix = '/'
    route_base = ''

    #def before_request(self, name):
    #   pass

    def after_request(self, name, response):
        return response

    def index(self):
        html = render_template('index.jinja')
        return html, 200

#IndexView.register(current_app)


