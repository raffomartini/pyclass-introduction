'''
Object-Oriented Programming
Why? How?

Introspection
	Using code to access variables' metadata

Information Hiding
	Reduces the amount of informations you need to keep in your head
	and makes it easier to change implementations details while staying
	backwards-compatible

Polymorphism
	Using the same name for methonds or attributes on different classes to
	avoid long chains if/elif/else

Inheritance
	Adding a lookup layer.
	Just a tool to re-use code instead of copy-pasting the same code across
	many classes.

Override
	Shadowing a methond or attribute of a parent class on a child class.

Magic Methods
	Special dunder (__name__) names that help you hook into the syntax tools.
	 Like operators and reserved words.
'''


'''
This is how you were doing it in c..

def dog_talk(name):
	print 'Woof! {} is barking.'.format(name)

def cat_talk(name):
	print 'Meow! {} is purring.'.format(name)

dog_a = 'Fido'
dog_b = 'Clifford'
cat_c = 'Socks'
'''

class Pet(object):
	'animals in the house'

	def __init__(self, name):
		self.name = name

class Dog(Pet):
	'our best friends'

	def __init__(self, name, age=None):
		Pet.__init__(self, name) # would have worked as well
		# print super(Dog)
		super(Dog, self).__init__(name)
		self.age = age

	def talk(self):
		print 'Woof! {} is barking.'.format(self.name)


class Cat(Pet):
	'semi-domestic animal'

	def __init__(self, name):
		self.name = name

	def talk(self):
		print 'Meow! {} is purring.'.format(self.name)

class Fish():
	pass


a = Dog('Fido')
#a.name = 'Fido'

b = Dog('Clifford')
# b.name = 'Clifford'

c = Cat('Socks')
# c.name = 'Socks'

d = Fish()


pets = [ a,b,c]
for pet in pets:
	# if isinstance(pet, Dog):
	# 	pet.talk()
	# elif isinstance(pet, Cat):
	# 	pet.talk()
	# else:
	# 	raise TypeError('Unknown pet type')
	# polymorphysm happened
	pet.talk()

# d.talk() # -> will raise attribute error

