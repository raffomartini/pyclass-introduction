'''
The date of oldest email in Ken Lay's inbox
'''
import re
from datetime import datetime

PATTERN = r'Date: .*, (.* .* .* .*:.*:.*) -?.* \(.*\)'

with open('notes/enron.lay-k.inbox.sample') as f:
    text = f.read()


timestrings = re.findall(PATTERN, text)
timestamps = []
for s in timestrings:
    ## datetime.strptime is converting that string into a datetime object
    ## for the format string you need to check the documentation
    timestamps.append(datetime.strptime(s, '%d %b %Y %H:%M:%S'))

print min(timestamps)
print max(timestamps)


# Task 2: How many US phone numbers are in the email?
numbers = re.findall(r'\(?[2-9]\d\d\)?[ /._\-]\(?\d{3}\)?[ /._\-]\(?\d{4}\)?', text)
print 'Total phone numbers', len(numbers)
print 'Unique phone numbers', len(set(numbers))
