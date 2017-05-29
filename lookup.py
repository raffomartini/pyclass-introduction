'''
Lookups

attributes      instance --> class --> AttributeError

variables       locals() --> globals()--> __builtins__ --> NameError
Note: variables are pointing to objects, functions are objects --> variable points to objects

imports         current working directory --> ... sys.path ... --> ImportError
'''

defaults = {
	'bg' : 'black',
	'fg' : 'green',
	'h' : 24,
	'w' : 80,
}

settings = {'h' : 40, 'fg' : 'cyan'}

user = {'fg': 'magenta'}

def lookup(key, primary, fallback):
	"""
	Assigns a set of keys based on settings and uses defaults if not found
	:param key:
	:param primary:
	:param fallback:
	:return:
	"""

	# EAFP: Easier to Ask Forgiveness than Permission
	# The Pythonic Way!

	try:
		return primary[key]
	except KeyError:
		return fallback[key]

def lookup(key, *dictionaries):
	for d in dictionaries:
		try:
			return d[key]
		except KeyError:
			continue
	raise KeyError(key)
