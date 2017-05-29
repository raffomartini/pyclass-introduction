'''
HTML parsing
'''

import notes
## a directory can be imported if the file __init__.py exsist

## BeautifulSoup is anther folder, the interesting file is BeautifulSoup.py
from notes.BeautifulSoup import BeautifulSoup

with open('notes/alltimegross.html') as f:
    html = f.read()

soup = BeautifulSoup(html)

# in well formatted html, id are unique
# <div id="main">
content = soup.find('div', id='main')
records = []
for row in content.findAll('tr'):
    record = []
    for cell in row.findAll('td'):
        record.append(cell.text)
    records.append(record)


