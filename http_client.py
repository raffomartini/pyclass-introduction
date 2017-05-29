'''
A simple TCP client
Transmission Control Protocol
'''

import socket

host = 'www.cisco.com'
port = 80
resource = '/'

s = socket.socket()

address = (host, port)
s.connect((host, port))

# build the GET request, note that HTTP requires \r\n
# it is adding headers
request = 'GET {} HTTP/1.1\r\n'.format(resource)
request += 'Host: {}\r\n'.format(host)
request += 'User-Agent: Crapaware\r\n'
request += 'Accept-Encoding: gzip\r\n'
request += 'Connection: close\r\n'
request += '\r\n'

s.sendall(request)

data=[]
while True:
	chunk = s.recv(4096)
	# when the stream finished an empty string is returned
	if not chunk:
		break
	data.append(chunk)
response = ''.join(data)

separator = '\r\n' * 2
header, content = response.split(separator,1)

if 'Content-Encoding: gzip' in header:
	# conditional import, it will import gzip only if the page is gzip encoded
	from gzip import GzipFile
	from StringIO import StringIO
	fakefile = StringIO(content)
	content = GzipFile(fileobj=fakefile).read()


