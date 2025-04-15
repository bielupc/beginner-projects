import socket

FORMAT = "utf-8"
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
HEADER = 64


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_msg(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b"" * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


while True:
    send_msg(input(">"))
