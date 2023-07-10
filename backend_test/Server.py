from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import eventlet

app = Flask(__name__, template_folder='templates')

socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print(f"Received message from client: {message}")
    response = f"You said: {message}"
    emit('message', response)

    # Spawn a new greenlet to send messages to the client
    eventlet.spawn(send_message_to_client)

def send_message_to_client():
    while True:
        # Send a message to the client
        socketio.send("This is a server-initiated message")

        # Delay between messages
        eventlet.sleep(5)

if __name__ == '__main__':
    socketio.run(app, host='localhost', port=8765)
