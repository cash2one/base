#/usr/bin/python

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('192.168.0.233',8001))
s.listen(10)
con,add = s.accept()
print 'con:',con
print 'add:',add

print add[0],"is connected"
print con.recv(512)
con.send('hello,I am the server')
s.close()
