## The Pythonic Way!

import random

names = [ 'Raffaello', 'Donatello', 'Michelangelo', 'Leonardo']
instruments = [ 'daggers', 'no-idea1', 'No-idea2', 'pole']

'''
for name in names:
	print name


print

for i,name in enumerate(names, 10):
	print i, name

print

for name in reversed(names):
	print name

for name, instrument in zip(names, instruments):
	print name, instrument

print
for size in map(len, names):
        print size
'''

def mymap(function, iterable):
        result = []
        for element in iterable:
                result.append(function(element))
        return result

## How Itearation Works

class Iterable:
	'an iterable can be for-looped'

	def __init__(self,maximum=0):
		self.maximum = maximum

	def __getitem__(self,index):
		if index >= self.maximum:
			raise IndexError(index)
		return index

class Iterator:
	'kind-of like the basic iterator type'

	def __init__(self, sequence):
		self.sequence = sequence
		self.current = 0

	# Fixed in python 3 as __next__
	def next(self):
		try:
			value = self.sequence[self.current]
		except IndexError:
			raise StopIteration
		self.current += 1
		return value

class Shuffled:
	'custom iterator for looping in random order'

	def __init__(self, sequence):
		self.sequence = sequence
		self.indeces = range(len(sequence))
		random.shuffle(self.indeces)

	def next(self):
		try:
			index = self.indeces.pop()
		except IndexError:
			raise StopIteration
		return self.sequence[index]

	# every iterator returns itself as an iterator
	def __iter__(self):
		return self