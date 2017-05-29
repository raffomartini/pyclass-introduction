import urllib
import re

url = 'https://pypi.python.org/pypi'
pattern = 'There are currently\s*<strong>(\d+)</strong>\s*packages here.'


response = urllib.urlopen(url)
html = response.read()

# normal first attempt
##print re.findall(pattern, html)

# better attempt
mo = re.search(pattern, html)

## mo.group(1) returns the first group, group 0 is the full matched string

print "There are {:s} packages in pypi".format(mo.group(1))



