import socket
from threading import Thread
import pickle
from os import system
from sys import platform


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


def clear():
    if platform == 'win32':
        system('cls')
    else:
        system('clear')


answer = input('/r to register, /l to login>')


if answer == '/r':

    login = input('login(username)>')
    password = input('password>')

    clear()

    client.send(pickle.dumps(['db.r', login, password]))

#   не работает

elif answer == '/l':
    login = input('login>')
    password = input('password>')

    clear()

    client.send(pickle.dumps(['db.l', login, password]))


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
