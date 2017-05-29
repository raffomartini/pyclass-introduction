'''
A multithreading TCP server
'''

HOST = 'localhost'
PORT = 9001

import socket
import time
from threading import Thread

def greeting(c, who):
	print 'received connection from', who
	c.sendall('Hello!')
	c.close()

def heartbeat(c, who):
	print 'received connection from', who
	for i in xrange(10):
		c.sendall(time.ctime())
		time.sleep(1)
	c.sendall('Bye')
	c.close()

def hardwork(c, who):
	print 'received connection from', who
	c.sendall('Doing hardwork!!!!!')
	sum(xrange(int(1e9)))
	c.sendall('DONE')
	c.close()

def server(handler, host=HOST, port=PORT):
	s = socket.socket()
	s.bind((host, port))
	s.listen(5)
	print 'listening for connections...'
	try:
		while True:
			c, who = s.accept()
			# handler(c, who)
			t = Thread(target=handler, args=(c, who))
			t.daemon = True # Kill a thread when the main thread dies
			t.start()
	except KeyboardInterrupt:
		print '\nGoodbye!'
	finally:
		s.close()


if __name__ == '__main__':
	# server(greeting)
	# server(heartbeat)
	server(hardwork)

