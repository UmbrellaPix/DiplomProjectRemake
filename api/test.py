from flask import make_response
from flask import jsonify

def test(server):
    @server.route('/test', methods=['GET'])
    def test():
        return make_response(jsonify({'OK': 'Request accept!'}), 200)