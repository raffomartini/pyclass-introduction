'''
A TCP server
'''

import socket
import time

def greeting(c, who):
	print 'received connection from', who
	c.sendall('Hello!')
	c.close()

def heartbeat(c, who):
	print 'received connection from', who
	for i in xrange(10):
		c.sendall(time.ctime())
		time.sleep(1)
	c.close()

def server(handler, host='localhost', port=9005):
	s = socket.socket()
	s.bind((host, port))
	s.listen(5)
	print 'listening for connections...'
	try:
		while True:
			c, who = s.accept()
			handler(c, who)
		# print 'received connection from', who
		# c.sendall('Hello!')
		# c.close()
	except KeyboardInterrupt:
		print '\nGoodbye!'
	finally:
		s.close()


if __name__ == '__main__':
	# server(greeting)
	server(heartbeat)

# s = socket.socket()

# address = 'localhost', 9002
# binds the server
# s.bind(address)
# listen on the configured port, the 5 is a "standard" value
# s.listen(5)
# print 'listening for connections...'
# accepts returns a tuple: a connection socket, and the source (tuple address, port)
# try:
# 	while True:
# 		c, who = s.accept()
# 		greeting(c,who)
# 		# print 'received connection from', who
# 		# c.sendall('Hello!')
# 		# c.close()
# except KeyboardInterrupt:
# 	print '\nGoodbye!'
# finally:
# 	s.close()


