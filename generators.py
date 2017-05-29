'''


List-version            Generator-version
						enumerate
						reversed
zip                     itertools.izip
map                     itertools.imap
sorted                  N/A
median                  N/A
f.readlines()           for line in f

# All generators are iterators generators are iterators that take minimize space

'''


# def count_to_three():
#
# 	# print 'a'
# 	yield 1
# 	# print 'b'
# 	yield 2
# 	# print 'c'
# 	yield 3
#
# g = count_to_three()

import random

def shuffled(seq):
	indices = range(len(seq))
	random.shuffle(indices)
	for i in indices:
		# print seq[i]
		yield seq[i]


def myipam(function, iterable):
	'''
	based on the mymap function
	def mymap(function, iterable):
        result = []
        for element in iterable:
                result.append(function(element))
        return result
	:param function:
	:param iterable:
	:return:
	'''

	for element in iterable:
		yield function(element)


def myipam(function, iterable):
	'''
	alternative way
	'''
	return (function(x) for x in iterable)
	# in python 3
	# yield from (function(x) for x in iterable)

'''
List comprehensions can be transformed in generators
List form:
In[3]: [s.upper() for s in 'hello']
Out[3]: ['H', 'E', 'L', 'L', 'O']

Generator form:
In[4]: (s.upper() for s in 'hello')
Out[4]: <generator object <genexpr> at 0x1051b9d20>

In[5]: for i in (s.upper() for s in 'hello'): print i
H
E
L
L
O
'''



def myenumerate(seq, start=0):
	current = start
	for element in seq:
		yield current, element
		current =+ 1