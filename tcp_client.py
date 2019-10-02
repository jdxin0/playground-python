import socket
import time
from ssl import SSLContext

sock = socket.socket()
sock.connect(('127.0.0.1', 10000))

sock.sendall(b'Hello, world')

#data = sock.recv(4048)

#time.sleep(10)

#print('Received', repr(data))