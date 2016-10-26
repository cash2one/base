#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.0.233',8001))
s.send('hello ,I am client')
print s.recv(512)
s.close()

