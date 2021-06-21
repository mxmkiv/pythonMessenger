import socket

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Жду подключения...')
    sock.bind(('8.8.8.8', 80))
    sock.listen(1)

    conn, addr = socket.accept()

    try:
        print('Соединение установлено', addr)
        while True:
            client_mes = conn.recv(1024).decode()

            if not client_mes:
                break

            print('Клиент:', client_mes)

            if client_mes == "exit":
                break

            conn.send(input('Сервер:')).encode()
            print()
    except Exception as err:
        print('error: ', err)
    finally:
        sock.close()