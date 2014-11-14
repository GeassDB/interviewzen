#!/usr/bin/env python
import socket

if __name__ == '__name__':
    s = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 900))
    s.listen(5)

    while 1:
        (clientsocket, address) = s.accept( )
        while True:
            data = clientsocket.recv(1024)
            if not data:
                break
            clientsocket.send(data)
        clientsocket.close()
