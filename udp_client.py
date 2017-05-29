'''
A simple UDP client.
User Datagram Protocol
'''

# interface into the OS socket
import socket
import time

'''
In[3]: socket.AF_INET
Out[3]: 2
'''

s = socket.socket(
		socket.AF_INET,
		socket.SOCK_DGRAM)

address = 'localhost', 9000
s.sendto('Hello?', address)
for i in xrange(10):
	s.sendto(time.ctime(), address)
	time.sleep(1)