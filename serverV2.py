import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('192.168.1.6', 8888))

server.listen(1)    # разрешение на 1 соединение
print('listening...')

while True:
    client_socket, addr = server.accept()
    print(f'[client info]: {client_socket}')

    client_socket.send("connect".encode('utf-8'))

    data = client_socket.recv(2048)

    print('[client]:', data.decode('utf-8'))

    message = input('>')

    if message == 'stop':
        client_socket.send('socket close'.encode('utf-8'))
        break

    else:
        client_socket.send(message.encode('utf-8'))

server.close()