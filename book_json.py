'''
Basic JSON
'''

import json

with open('notes/books.json') as f:
    books = json.load(f)

# print the price of the book if bk111
print books['bk111']['price']

stuff = {'a' : 1, 'b' : [10,20,30], 'c': {'another' : 'nested'}}

## convert the dictionary to json
print json.dumps(stuff, indent=2)

