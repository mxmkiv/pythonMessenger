import pickle
import socket
import threading
import pymysql
from config import *

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=db_user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print('db connect')
except Exception as ex:
    print('Error db connect...')
    print(ex)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('192.168.1.6', 8888))

server.listen(1)    # разрешение на 1 соединение
print('listening...')

users = []


def send_all(data):
    for user in users:
        user.send(data)


def listen_user(user):
    print('listening user')

    while True:
        data = user.recv(2048)
        #   print(f'[client]: {data}')

        print(pickle.loads(data)[0], ':', pickle.loads(data)[1])

        #   print('[client]:', data.decode('utf-8'))
        send_all(data)


def start_server():
    while True:
        user_socket, addr = server.accept()
        print(f'[info]: {addr[0]} connect')

        users.append(user_socket)
        listen_accept_user = threading.Thread(
            target=listen_user,
            args=(user_socket,)
        )

        listen_accept_user.start()


if __name__ == '__main__':
    start_server()
