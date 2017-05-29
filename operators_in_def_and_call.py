'''
Calling functions

Operator    Mode    Purpose
=           def     default value
BE CAREFULL WHEN USING CONTAINERS TO SET A DEFAULT
=           call    keyword argument

*           def     pack positional arguments in a tupple
*           call    unpack a sequence of positional argments

**          def     pack keyword arguments into a dict
**          call    unpack a dict as keyword arguments
'''

def power(base):
	return base ** 2

def power(base, exponent=2):  # make calls more pleasant
	return base ** exponent   # added features, keeps bakwards compatibility

# interesting way to do multi lines function calls
print power(
	base=5,
	exponent=3,
	)

# * in a function call will unpack a sequence as positional args
x = [5,3]
print power(*x)


# ** in a function call will unpack a dictionary as keyword args
y = {
	'base' : 5,
	'exponent' : 3,
}

print power(**y)

# define *args
def foo(*args):
	print args

print foo(1,2,3)

# define **kwargs
def foo(**kwargs):
	print kwargs




