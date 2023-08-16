from flask import Flask
from flask import make_response
from flask import jsonify
from flask_cors import CORS
import os

server = Flask(__name__)
CORS(server, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

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
server.run(host = '127.0.0.1', port=2000,debug=True)