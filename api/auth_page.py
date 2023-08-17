from flask import make_response, Response
from flask import jsonify
from flask import request
from modules.memory.memory import User


def auth_page(server):
    @server.route('/auth_page', methods=['POST'])
    def auth_page():
        data = request.get_json()
        if 'login' not in data or 'password' not in data:
            return make_response('Login and password are required', 401)

        user_id = server.auth_login(data['login'], data['password'])
        if user_id == 0:
            return make_response('Invalid credentials', 401)

        token = server.create_session(user_id)
        
        response = make_response("", 200)
        response.headers.add('Authorization', token)
        return response