import socket


"""def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]"""


if __name__ == "__main__":

    sock = socket.socket()

    print("IP: {}. Жду подключения...")
    sock.bind(("", 9090))
    sock.listen(2)

    conn, addr = sock.accept()

    try:
        print("Соединение установлено:", addr)
        while True:
            # отправка сообщений
            # со стороны клиента
            client_mes = conn.recv(1024).decode()
            if not client_mes:
                break

            print("Клиент:", client_mes)
            if client_mes == "Выход":
                break

            conn.send(input("Сервер: ").encode())
        print("Соединение закрыто.")
    except Exception as err:
        print("Ошибка: ", err)
    finally:
        conn.close()