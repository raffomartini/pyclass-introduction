'''
Special Methods

http://www.rafekettler.com/magicmethods.html
https://docs.python.org/2/reference/datamodel.html

Operator/Function/Keyword       Magic Method(s)             Description
s + t                           s.__add__(t)                addable
s / t                           s.__div__(t)                divisible
s == t                          s.__eq__(t), s.__cmp__(t)   equal # by default uses is()
<, >, <=, >=    				s.__comp__(t)

str(o), print o                 o.__str__()
repr(o), >>> o                  o.__repr__()
len(o)                          o.__len__()

s[t]                            o.__getitem__(t)            indexable
s[t:u]                          __getitem__, __getslice__   sliceable
iter(s), for u in s             __iter__, __getitem__       iterable
'''


class Dog:
	'our best friends'

	def __init__(self, name):
		self.name = name

	# to represent the dog
	def __repr__(self):
		# return 'Dog(%r)' % self.name
		return 'Dog({!r})'.format(self.name)

	def bark(self):
		return 'Woof! I am {}'.format(self.name)

	def __add__(self, other):
		return Dog('{}, Jr.'.format(self.name))

	def __eq__(self,other):
		return self.name == other.name

	def __comp__(self,other):
		return cmp(self.name, other.name)

class Kennel:
	'a place to store dogs'

	def __init__(self, dogs=[]):
		if dogs is None:
			self.dogs = []
		self.dogs = dogs

	def board(self, dog):
		self.dogs.append(dog)

	def __repr__(self):
		return 'Kennel({!r})'.format(self.dogs)

	def __len__(self):
		return len(self.dogs)

	def __getitem__(self, index ):
		return self.dogs[index]

	def __iter__(self):
		return iter(self.dogs)

# print 'My name is', __name__

# this is used to create a main scope in the module
if __name__ == '__main__':
	k = Kennel()
	k.board(Dog('Fido'))
	k.board(Dog('Clifford'))
	k.board(Dog('Pluto'))
