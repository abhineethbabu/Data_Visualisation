from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random
import time
from threading import Thread

app = Flask(__name__)
socketio = SocketIO(app)
#  i = 0
def generate_random_value():
    # arr =[]
    arr = [random.randint(1, 100),random.randint(1, 100)]
    # i+=1
    return arr

def emit_random_value():
    while True:
        random_value = generate_random_value()
        socketio.emit('update', {'random_value': random_value})
        time.sleep(0.025)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

if __name__ == '__main__':
    update_thread = Thread(target=emit_random_value)
    update_thread.daemon = True
    update_thread.start()
    socketio.run(app)


