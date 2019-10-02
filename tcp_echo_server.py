import selectors
import socket


selector = selectors.DefaultSelector()


def read(conn, mask):
    try:
        data = conn.recv(1000)
    except ConnectionError as e:
        print(e)
        selector.unregister(conn)
        conn.close()
    else:
        if data:
            conn.send(data)
        else:
            print('closing', conn)
            selector.unregister(conn)
            conn.close()


def accept(sock, mask):
    conn, addr = sock.accept()
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    selector.register(conn, selectors.EVENT_READ, read)


sock = socket.socket()
sock.bind(('127.0.0.1', 10000))
sock.listen()
sock.setblocking(False)

selector.register(sock, selectors.EVENT_READ, accept)

while True:
    events = selector.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
