#!/bin/python

from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from rs485 import sendRs485

app = Flask(__name__)
api = Api(app)

class Listen(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('typ', type=str)
        parser.add_argument('mode', type=str)
        args = parser.parse_args()

        name = args['name']
        typ = args['typ']
        mode = args['mode']
        
        sendRs485(name,typ,mode)

        return {'name' : name, 'typ' : typ, 'mode' :mode}

api.add_resource(Listen, '/req')

if __name__ == '__main__':
    app.run(
            host = "0.0.0.0",
            port = 8998
            )
