# encoding=utf-8
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


# 确认客户端已经接受，开始删除消息列表中的消息
def ack():
    print('message was received!')


@socketio.on('client_event')
def client_msg(msg):
    # 向所有客户端发送广播
    socketio.emit('server_response', {'data': msg['data']})


@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json, callback=ack)
    return json


if __name__ == '__main__':
    # 172.29.30.108
    socketio.run(app, host='0.0.0.0', port=5000)
