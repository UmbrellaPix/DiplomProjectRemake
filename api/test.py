from flask import make_response
from flask import jsonify

def test(server):
    @server.route('/test', methods=['GET'])
    def test():
            response = make_response(jsonify({'OK': 'Request accept!'}), 200)
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response