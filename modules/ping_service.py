from flask import Flask, redirect, request
from flask_restful import reqparse, abort, Resource, fields, marshal_with
from utils.utils import Utils
import time



class PingService(Resource):

    def get(self, service_name):
        if service_name == 'me':
            return {'status': Utils.uptime(), 'timestamp': int(time.time())}
        status = Utils.ping("home.knnect.com")
        return {'status': status, 'timestamp': int(time.time())}
     
    def post(self, service_name):
        return {'submitted': True}
