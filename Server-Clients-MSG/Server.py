import socket
import threading

FORMAT = "utf-8"
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def control_clients(conn, addr):
    print("[NOVA CONNEXIÓ] {} s'ha connectat".format(addr))
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if (msg == DISCONNECT_MESSAGE):
            print("[DESCONEXIÓ] {} s'ha deconectat".format(addr))
            connected = False
        else:
            print("[{}] {}".format(addr, msg))
    conn.close()

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=control_clients, args=(conn, addr))
        thread.start()

print("[INICIALITZANT] El servidor s'està iniciant a {}...".format(ADDR))
start()

