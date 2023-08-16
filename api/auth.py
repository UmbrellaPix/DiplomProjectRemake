from flask import make_response
from flask import jsonify
from flask import request
from modules.memory.memory import User


def auth(server):
    @server.route('/auth', methods=['POST'])
    def auth():

            response = make_response(jsonify({'OK': 'Request accept!', 'test':'test'}), 200)
            return response