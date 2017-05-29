"""
Show all interfaces that are up
"""

# Idea: use a slice[start:stop]
# save parsed records for further analysis later
# pick colomns from header

with open('notes/ipv4_int_bri.txt') as f:
    for line in f:
        name = line[:31].rstrip()
        address = line[31:47].rstrip()
        status = line[47:69].rstrip()
        protocol = line[69:].rstrip()
##      initial code
##        name, address, status, protocol = line.split()
        if status.lower() == protocol.lower() == 'up':
            print '{:30s}{:30}'.format(name, address)
