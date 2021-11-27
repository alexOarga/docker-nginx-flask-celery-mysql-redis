import eventlet
eventlet.monkey_patch()

import os
import logging.config

from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_socketio import join_room
from .database import db

from src.app.blueprint.example_bp import example_bp
from src.app.exception_handler import init_exception_handler

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# Logger config
logging.config.dictConfig(app.config["DICT_LOGGER"])

# Database config
db.init_app(app)

# Register blueprints
app.register_blueprint(example_bp, url_prefix='/')

# Register exception handlers
init_exception_handler(app)

# Init websockets
socketio = SocketIO(app, \
                    message_queue=app.config['REDIS_BROKER_URL'])


@app.errorhandler(404)
def page_not_found(e):
    response = jsonify({'message': "Not found"})
    response.status_code = 404
    return response

@app.route('/hello/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@socketio.on('connect')
def test_connect():
    # Client connected via socketio
    pass

@socketio.on('join')
def on_join(room_name):
    # Client joined room via socketio
    join_room(room_name)

if __name__ == '__main__':
    socketio.run(app)
