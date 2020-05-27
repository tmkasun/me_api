from flask import Flask, redirect, request
from flask_restful import reqparse, abort, Resource, fields, marshal_with
from utils.utils import Utils
import time



class PingService(Resource):

    def get(self, service_name):
        if service_name == 'me':
            return {'status': Utils.uptime(service_name), 'timestamp': int(time.time())}
        elif service_name == 'dell':
            status = Utils.ping("plex.knnect.com")
            return {'status': status, 'timestamp': int(time.time())}
        return {'status': False, 'timestamp': int(time.time())}
        
     
    def post(self, service_name):
        return {'submitted': True}
