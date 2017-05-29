'''
Basic XML
ElementTree supports most of the XPATH spec.

element.get(attribute_name)
eleming.find('tag_name')
element.text (normally not useful except in the inner most lib)
'''

from xml.etree import ElementTree

tree = ElementTree.parse('notes/books.xml')

catalog = tree.getroot()

for book in catalog.findall('book'):
    if book.get('id') == 'bk108':
        author = book.find('author')
        print author.text

for price in catalog.findall('book/price'):
    print price.text
