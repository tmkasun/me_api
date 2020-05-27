from flask import Flask, redirect, request
from flask_restful import reqparse, abort, Resource, fields, marshal_with
from utils.utils import Utils
from werkzeug.exceptions import BadRequest
import time


class OperationsService(Resource):

    def get(self, server_id):
        if server_id == 'dell':
            Utils.wakeOnLan()
            return {'status': True, 'timestamp': int(time.time())}
        else:
            return {'status': False, 'timestamp': int(time.time())}

    def post(self, server_id):
        status = False
        try:
            if request.json:
                payload = request.json
                operation = payload['operation']
                if operation == 'wakeonlan':
                    status = Utils.wakeOnLan(server_id)
                elif operation == 'poweroff':
                    status = Utils.powerOff(server_id)
            return {'status': status, 'timestamp': int(time.time())}
        except BadRequest as error:
            print("Not in json format BAD Request")
            return {'status': status, 'timestamp': int(time.time())}
