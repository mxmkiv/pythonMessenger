import socket
import pymysql
import config
from threading import Thread
import pickle


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('192.168.1.6', 8888))

username = input('name>')


'''answer = input('sign in or sign up')
if answer == 'sign in':
    username = input('username>')
    password = input('password>')
    
elif answer == 'sign up':
    name = input('name>')
    username = input('username>')
    password = input('password>')'''


def listen_server():
    while True:
        data = client.recv(2048)

        if pickle.loads(data)[0] == username:
            continue
        else:
            print(pickle.loads(data)[0], ':', pickle.loads(data)[1])
        #   (data.decode('utf-8'))


def send_server():
    listen_thread = Thread(target=listen_server)
    listen_thread.start()

    while True:
        message = input('')

        send_data = [username, message]
        obj = pickle.dumps(send_data)
        client.send(obj)
        #   client.send(input('>').encode('utf-8'))


if __name__ == '__main__':
    send_server()
