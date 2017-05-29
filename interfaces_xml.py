'''
XML with namespaces
'''

from xml.etree import ElementTree

# namespaces copied from the xml file
ns = {'nf': 'urn:ietf:params:xml:ns:netconf:base:1.0',
      'default' : 'http://www.cisco.com/nxos:1.0:if_manager'}

tree = ElementTree.parse('notes/interfaces.xml')
rpc_reply = tree.getroot()

# needs the namespace definition to find anything
print rpc_reply.find('nf:data', ns)

for addr in tree.findall('.//default:eth_hw_addr', ns):
    print addr.text


                    
