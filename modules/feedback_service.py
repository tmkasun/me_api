from flask import Flask, redirect, request
from flask_restful import reqparse, abort, Resource, fields, marshal_with

from datetime import datetime
import time
from .mail_sender import create_message, getServiceClient, send_message

parser = reqparse.RequestParser()
# If the argument location list includes the headers location the argument names will no longer be case insensitive
# and must match their title case names (see str.title()).
# Specifying location='headers' (not as a list) will retain case insensitivity.
parser.add_argument('User-Agent', location='headers')
parser.add_argument('host', location='headers')

NO_REPEAT = 20000
parser.add_argument('score', location='json')
parser.add_argument('check', location='json')
parser.add_argument('message', location='json')


class FeedbackService(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = getServiceClient()

    def get(self):
        print(request.remote_addr)
        return redirect("https://wso2.com/api-management/", 302)
    # in-house CORS handler

    def options(self):
        return {'Allowed': True}, 200, {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'POST',
                                        'Access-Control-Allow-Headers': 'Host, Content-Type'}

    def post(self):
        args = parser.parse_args()
        if not args['check']:
            return {'check': False}
        check = int(args['check'])
        if(time.time()*1000 - check > NO_REPEAT):
            return {'check': False}
        with open('./resources/template.html', 'r') as html_template:
            template_content = html_template.read()
            template_content = template_content.replace(
                '{#location}', request.remote_addr)

            template_content = template_content.replace(
                '{#browser}', request.user_agent.browser)

            template_content = template_content.replace(
                '{#browserversion}', request.user_agent.version)

            template_content = template_content.replace(
                '{#platform}', request.user_agent.platform)

            template_content = template_content.replace(
                '{#language}', request.accept_languages.best)

            template_content = template_content.replace(
                '{#score}', args['score'])
            template_content = template_content.replace(
                '{#message}', args['message'])
            template_content = template_content.replace(
                '{#time}', datetime.now().strftime("%I:%M%p on %B %d, %Y"))
            e_message = create_message(
                "tmkasun2@gmail.com",
                'tmkasun@gmail.com',
                'Keels availability', template_content)
            ack = send_message(self.service, 'me', e_message)
        return {'submitted': True}
