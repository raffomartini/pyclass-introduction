'''
Analyzing the Kaprekar process
'''

def step(x):
	'''
	One step in the Kaprekar process.
	0. Take a 4-digit number
	1. Sort the digits in ascending order
	2. Sort the digits in descending order
	3. return ascending - descending

	>>> step(3764)
	4176
	>>> step(4176)
	6174
	>>> step(6174)
	6174

	:param x:
	:return:
	'''
	zero_padded = "{:04d}".format(x)
	ascending = int(''.join(sorted(zero_padded)))
	descending = int(''.join(sorted(zero_padded, reverse=True)))
	return descending - ascending

def gen_graph():
	"""
	Generate the dot-format (www.graphviz.org) representation of the Kaprekar process
	for all the 4-digit number

		Usage on Mac:
        $ python kaprekar.py | dot -Tsvg > kaprekar.svg
        $ open -a Safari kaprekar.svg
	:return:
	"""
	graph = {}


	for n in range(10000):
		graph['{:04d}'.format(n)] = '{:04d}'.format(step(n))

	sources = set(graph.keys()) - set(graph.values())
	rest = set(graph.keys()) - sources

	groups = {}
	for leaf in sources:
		target = graph[leaf]
		try:
			groups[target].add(leaf)
		except KeyError:
			groups[target] = {leaf}

	print '''
	digraph {
		graph [rankdir=LR]
	'''

	for n in sorted(rest):
		print '{:s} -> {:s};'.format(n, graph[n])

	print 'node [shape=rectangle];'
	for target, group in sorted(groups.items()):
		label = '"{} ..."'.format(', '.join(sorted(group)[:3]))
		print '{} -> {} [label={}];'.format(label, target, len(group))

	print '}'

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	gen_graph()
