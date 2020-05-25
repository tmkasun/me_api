# from modules.feedback_service import FeedbackService
from modules.ping_service import PingService
from flask import Flask
from flask_restful import Api
from flask import request
import re

app = Flask(__name__)
api = Api(app)
# api.add_resource(FeedbackService, '/apis/feedbacks')
api.add_resource(PingService, '/apis/ping/<service_name>')

# in-house CORS handler
cors_origin_pattern = re.compile(".*\.knnect\.com")
@app.after_request
def post_request_handler(response):
    try:
        matched = cors_origin_pattern.match(request.origin)
        if matched:
            response.access_control_allow_origin = request.origin
            response.access_control_allow_methods = [request.method]
            response.access_control_allow_headers = list(request.headers.keys())
        return response
    except AttributeError:
        print("No origin header")
        return response

# Uncomment below for testing locally
# app.run()

def main():
    app.run(host='0.0.0.0', port=9900)
    pass


if __name__ == '__main__':
    main()

# Sample curl
# curl -kv -X POST http://localhost:5000/apis/feedbacks -d '{"check": "1569866131827","score":"1", "message": "greate software"}' -H "Content-Type: application/json"
