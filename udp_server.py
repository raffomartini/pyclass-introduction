'''
A simple UDP server.
User Datagram Protocol
'''

import socket

'''
In[3]: socket.AF_INET
Out[3]: 2
'''

s = socket.socket(
	socket.AF_INET,
	socket.SOCK_DGRAM)

address = 'localhost', 9000
s.bind(address)
try:
	while True:
		data, who = s.recvfrom(4096)
		print data, who
except KeyboardInterrupt:
	print '\nGoodbye!'
finally:
	s.close()
