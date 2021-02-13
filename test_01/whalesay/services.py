from test_01.whalesay.api import api
from test_01.whalesay.thewhale import Whale
from flask_restplus import Resource
from flask import Response

@api.route('/whalesay/<message_id>')
class HelloWorld(Resource):
    def get(self, message_id):
        whale = Whale()
        return Response(whale.talk(message_id), mimetype="text/plain")
