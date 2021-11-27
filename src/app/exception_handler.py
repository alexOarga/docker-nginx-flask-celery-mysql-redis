from flask import jsonify

def init_exception_handler(app):
    app.register_error_handler(RuntimeError, handle_runtime_error)

def handle_runtime_error(error):
    response = jsonify({'message': "Internal server error"})
    response.status_code = 500
    return response