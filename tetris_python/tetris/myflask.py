from flask import Flask , render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'BCODE_Flask'
socketio = SocketIO(app)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/tetris")
def tetris():
    return render_template("tetris_network.html")

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)
    
if __name__ == '__main__':
    socketio.run(app, host = "192.168.43.46", port=5000)
    
    
# pip install --upgrade python-socketio==4.6.0
# pip install --upgrade python-engineio==3.13.2
# pip install --upgrade Flask-SocketIO==4.3.1