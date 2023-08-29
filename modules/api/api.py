from flask import Flask
from flask import make_response
from flask import jsonify
from flask_cors import CORS
import os
from modules.memory.functions import auth_token, create_session, auth_login

from waitress import serve

server = Flask(__name__)
CORS(server, resources={r"/*": {"origins": "*", "supports_credentials": True}}, expose_headers=["Authorization"])

server.create_session = create_session
server.auth_token = auth_token
server.auth_login = auth_login

@server.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# Подключение всех API из ./api
server.api = []
for entry in os.scandir(path="./api"):
    if entry.is_file():
        try:
            string = f'from api.{entry.name}'[:-3] + f' import {entry.name}'[:-3]#создание строки с командой импорта
            exec(string)

            string = f'{entry.name}'[:-3] + '(server)'
            exec(string)

            print(f'Load: {entry.name} api')
        except Exception as err:
            print(f'ERROR API LOADE:{err}')

server.config['SECRET_KEY']='LongAndRandomSecretKey'
serve(app = server, host = '192.168.0.10', port=2000, threads=1)