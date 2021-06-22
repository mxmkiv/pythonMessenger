import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('192.168.1.6', 8888))

while True:
    server_data = client.recv(2048)
    print('[server]:', server_data.decode('utf-8'))

    message = input('>')

    if message == 'exit':
        client.send("client disconnect".encode('utf-8'))
        break

    else:
        client.send(message.encode('utf-8'))