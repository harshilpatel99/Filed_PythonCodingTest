import os

from flask import Flask, make_response, jsonify, request
from flask import g
from dal.db import Db
from transaction.process_transaction import Process_Transaction
from exception.app_exception import AppException, ClientException, ServerException

import config

process_transaction = Process_Transaction()
app = Flask(__name__)
app.config.from_object(config.Config)


@app.errorhandler(AppException)
def app_error(err):
    app.logger.exception(err)
    return make_response(jsonify(err.error), err.http_code)

@app.errorhandler(Exception)
def handle_generic_error(err):
    app.logger.exception(err)
    return make_response(jsonify(str(err)), 500)

@app.route('/process_payment', methods=['POST'])
def process_payment():
    data = request.get_json()
    result, code = process_transaction.initialize_payment(data)
    return make_response(jsonify(result),code)

def init_app(flask_app):
    flask_app.config.from_object(config.DEVConfig)
    db_instance = Db(flask_app)
    print('DB Connection: ' + str(db_instance))


if __name__ == '__main__':
    init_app(app)
    app.run(host='127.0.0.1', port='5000')
