from flask import make_response
from flask import jsonify
from flask import request
from flask import Response
# from modules.memory.functions import auth_token

def auth_token(server):
    @server.route('/auth_token', methods=['GET'])
    def auth_token():
        authorization_header = request.headers.get("Authorization")
        status_code = 200
        response_data = Response()

        if authorization_header:
            token = authorization_header.split(" ")[-1]
            auth = server.auth_token(token)
            if auth:
                response_headers = {"Authorization": "true"}
            else:
                response_headers = {"Authorization": "false"}
                status_code = 401
        else:
            response_headers = {}
            status_code = 400

        response = make_response(response_data, status_code)
        response.headers.extend(response_headers)
        return response