from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print(f"Received message from client: {message}")
    response = f"You said: {message}"
    emit('message', response)

if __name__ == '__main__':
    socketio.run(app, host='localhost', port=8765)
s