#!/usr/bin/env python
#coding:utf-8
'''
    这是一个简单模拟的memcache的客户端
	首先你需要安装memcache服务端
	然后启动memcache服务，端口为11211
'''
import os
import sys
import socket

SERVER_MAX_KEY_LENGTH = 250  

SERVER_MAX_VALUE_LENGTH = 1024 * 1024
 
MAX_DATA_LENGTH = 1024 * 1024
 
LOCALHOST = '127.0.0.1'

DEFAULT_PORT = 11211

DEFAULT_ADDRESS = (LOCALHOST, DEFAULT_PORT)

class Client:
 
    def __init__(self, url):
        self.url = url
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #建立socket连接
        self.cmdlog = []
        self.cmd = None
 
        try:					#异常处理
            a_url, a_port = self.url.split(':')
            addr = (a_url, int(a_port))
            self.sock.connect(addr)
        except socket.error, msg:
            print('Connecting %s error' % msg[1])
            sys.exit(1)
 

    ###  set  get  ###
    def set(self, key, value, flags=0, expired=0):	#set,数据缓存处理
        self.cmd = '%s %s %d %d %d\r\n%s\r\n' % (
            'set', key, flags, expired, len(value), value)
        self.cmdlog.append(self.cmd)
        self.sock.sendall(self.cmd.encode())
        data = self.sock.recv(MAX_DATA_LENGTH)
        return data

    def get(self, key):					#get,数据获取
        self.cmd = '%s %s\r\n' % ('get', key)
        self.cmdlog.append(self.cmd)
        self.sock.sendall(self.cmd.encode())
        data = self.sock.recv(MAX_DATA_LENGTH)
        return data


if __name__ == '__main__':
    mc = Client('127.0.0.1:11211')		#实例测试
    mc.set('test', 'this is just a test!')
    mc.set('demo', 'this is just a demo!')
    data = mc.get('test')
    print data
    data1 = mc.get('demo')
    print data1
