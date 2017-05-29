'''
A simple TCP client
Transmission Control Protocol
'''

import socket
import time

HOST = 'localhost'
PORT = 9005

s = socket.socket()
	# TCP is the default
	# socket.AF_INET,
	# socket.SOCK_STREAM)

address = HOST, PORT
s.connect(address)
while True:
	data = s.recv(4096)
	# when the stream finished an empty string is returned
	if not data:
	# if  data == '':
		break
	print data