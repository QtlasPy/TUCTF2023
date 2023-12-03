import socket


def ajouter(s : socket.socket, index : int) -> None:
    "Ajoute 1 a l'index : index"

    s.send('1\n'.encode())
    msg = s.recv(256).decode()
    s.send((str(index) +'\n').encode())
    msg = s.recv(256).decode()
    s.send((str('+') + '\n').encode())
    msg = s.recv(2048).decode()
    if msg.find('The chest is still locked!') == -1:
        print(msg)
        exit(0)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = "chal.tuctf.com"
server_port = 30002

s.connect((server_addr, server_port))

while True:
    data = s.recv(256).decode()
    print(data)

    for i in range(10):
        for l in range(10):
            for _ in range(10):
                ajouter(s, 3)
            ajouter(s, 2)
        ajouter(s, 1)
