import socket
import threading
from queue import Queue


target = input("Enter the IP you want to target:")

q = Queue()
for x in range(1,501):
    q.put(x)

def portscanner(port):
    try:
        s = socket.socket(socket.AF_INET,
                          socket.SOCK_STREAM)
        conn = s.connect((target, port))
        return True
    except:
        return False

def worker():
    while True:
        port = q.get()
        if(portscanner(port)):
            print("Port {} = open".format(port))


for x in range(400):
    t = threading.Thread(target=worker)
    t.start()


