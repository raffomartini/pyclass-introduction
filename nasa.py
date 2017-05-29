'''
Analysing the NASA weblogs

Steps to suscess (if the data is small enough):
1. Collect the data
2. Parse the data into a useful data structure
3. Analyse / process the data

Steps to success (if the data is too large):
1. get a stream of data
2. process the stream with tiny generators, each flowing to the next
3. Aggregate or simply output in different format the data
'''

import collections
import re
from collections import Counter, namedtuple

Log = namedtuple('Log','address timestring request status size')

# Task1: Most frequent visitors?
# counts = {}
# counts = collections.Counter()
# with open('notes/nasa.log.sample') as f:
# 	for line in f:
# 		address = line.split(' - - ')[0]
# 		# the get method returns Null if the key is not found, the return can be
# 		# overridden
# 		# counts[address] = counts.get(address, 0) + 1
# 		counts[address] += 1
#
# print counts.most_common(3)


# sorted, min, max accepts a keymap function as key argument
# the keymap can be used to change the imput collection
# in this case we use a lambda function that maps the elements in items() and returns
# the value
# so we are sorting on the items in counts, mapped with the lambda function, in reverse
#  (from top to bottom)
# In[18]: sorted(counts.items(), key=lambda p: p[1], reverse=True)[:3]
# Out[17]:
# [('piweba3y.prodigy.com', 14),
#  ('edams.ksc.nasa.gov', 11),
#  ('piweba4y.prodigy.com', 10)]

# even better way:
#sorted(counts, key=lambda p: counts[p], reverse=True)[:10]

# Task 2: compare frequency of visits by hour of day

# counts = collections.Counter()
# with open('notes/nasa.log.sample') as f:
# 	for line in f:
# 		hour = line.split(':')[1]
# 		# the get method returns Null if the key is not found, the return can be
# 		# overridden
# 		# counts[address] = counts.get(address, 0) + 1
# 		counts[hour] += 1

def bar_chart(counts):
	for hour, count in sorted (counts.items()):
		# print hour, count
		# better representation
		print hour, count / 3 * '#'

# Task 3: Parse (mostly) everythin useful from the log using regex

# pattern = r'(.*) - - \[(.*)\] "(.*)" (.*) (.*)'
# records = []
#
# with open('notes/nasa.log.sample') as f:
# 	for line in f:
# 		mo = re.search(pattern, line)
# 		if mo is not None:
# 			records.append(mo.groups())
# 		break


def parselogs(filename):
	'''
	This was initially using a list, it then become a generator
	Commented lines are what used to be a list
	:param filename:
	:return:
	'''
	pattern = r'(.*) - - \[(.*)\] "(.*)" (.*) (.*)'
	# records = []
	with open('notes/nasa.log.sample') as f:
		for line in f:
			mo = re.search(pattern, line)
			if mo is not None:
				# address, timestring, request, status, size = mo.groups()
				# records.append(mo.groups())
				yield Log(*mo.groups())
	# return records

if __name__ == '__main__':

	FILENAME = 'notes / nasa.log.sample'
	# Task 1: Compare frequent visitors
	records = parselogs(FILENAME)
	visitors = (r.address for r in records)
	print Counter(visitors).most_common(3)

	# Task 2: Compare frequency by hour
	records = parselogs(FILENAME)
	# r = records[0]
	hours = (r.timestring.split(':')[1] for r in records)
	counts = Counter(hours)
	bar_chart(counts)


def repl():
	'Read Eval Print Loop'
	while True:
		source = raw_input('<<<< ')
		try:
			result = eval(source)
			print repr(result)
		except SyntaxError:
			exec source
