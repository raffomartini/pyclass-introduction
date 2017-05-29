'''Show how to use expect style functionality to access a Cisco device via telnet

   Notes:
      1) Pexpect is a third-party module (not part of the standard library).
  
         PExpect Download link:      https://pypi.python.org/pypi/pexpect/
         PExpect Documentation:      https://pexpect.readthedocs.org/en/latest/
         PExpect Examples:           https://bit.ly/pexpect

      2) The Pexpect module does not run on Windows because it depends on the
         Linux tty interface.

      3) You can accomplish something similar without pexpect or telnet
         using the standard library's socket module.  The socket.makefile()
         function lets you interface with a socket as if you were reading
         and writing lines to a file.   The socket.settimeout() function
         sets time limits on responses and can keep you application from
         appearing to hang when waiting for data.

     4)  Possible issue:  What if "#" appears in the data?
         Answer:  The data gets cut-off.

'''

import pexpect

def fetch_device_data(command, ipaddr, port, username='lab', password='lab'):
    child = pexpect.spawn('telnet %s %s' % (ipaddr, port), timeout=2)
    child.sendline('')
    try:
        child.expect('[Uu]sername: ')
        child.sendline(username)
        child.expect('Pass.*?:')
        child.sendline(password)
    except pexpect.TIMEOUT:
        pass
    child.expect('#')
    child.sendline('term len 0')         # turn-off "more" paging
    child.expect('#')
    child.sendline('term width 511')     # turn-off line wrapping
    child.expect('#')
    child.sendline(command)
    child.expect('#')
    data = child.before
    child.terminate()
    return data

data = fetch_device_data(command ='show ip interface br',
                         ipaddr = '172.27.170.184',
                         port = 2009)
for line in data.splitlines():
    fields = line.split()
    if len(fields) == 6:
        interface, ipaddr, ok, method, status, protocol = fields
        if status.lower() == 'up':
            print '%-15s %s' % (ipaddr, interface)

