from flask import Flask
from flask_socketio import SocketIO, emit
app = Flask(__name__)

socketio = SocketIO(app)

@socketio.on('connect')
def hello():
	emit("connected", broadcast=True)

@socketio.on("join_room")
def join(data):
	emit("joined", data)