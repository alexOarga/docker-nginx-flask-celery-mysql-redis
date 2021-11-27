from flask_socketio import SocketIO

socketio = SocketIO(message_queue='redis://')

# Send message to a specific room
# Note this can be called even inside a celery worker!
def send_message_client(room_name, message):
    socketio.emit(room_name, {'data': message}, to=room_name, room=room_name)
