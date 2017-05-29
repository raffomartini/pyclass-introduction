#! /usr/bin/env python
"""Download all the class files to a local directory.
By default will download files into a folder named "notes".

Usage:

Copy the text from this web page
and paste the text into a new plain text file,
then save the file as a Python script "download.py".

To execute this script with IDLE,
make sure this script is the currently active window,
then select the menu option "Run -> Run Module".

To execute this script via command line:

    $ python download.py
"""

from __future__ import print_function, division

import sys
if sys.version_info < (3, 0):
    from urllib2 import Request, urlopen, HTTPError
    from cStringIO import StringIO as PseudoFile
    import dumbdbm
else:
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    from io import BytesIO as PseudoFile
    from dbm import dumb as dumbdbm

import os, re, time, gzip, threading, ssl
from collections import namedtuple
from multiprocessing.pool import ThreadPool as Pool
from pprint import pprint
from argparse import ArgumentParser


class_name = '2016-02-29'
links_url_template = 'https://dl.dropboxusercontent.com/u/54337323/%s/links.txt'



Response = namedtuple('Response', ['code', 'msg', 'compressed', 'written'])



try:
    no_cert_context = ssl._create_unverified_context()
except AttributeError:
    no_cert_context = None



def get_header(urllib_connection, name):
    'get HTTP response header, compatibility function for Python 2.x and 3.x'
    if sys.version_info < (3, 0):
        return urllib_connection.info().getheader(name)
    return urllib_connection.getheader(name)



def urlretrieve(url, filename, cache={}, lock=threading.Lock()):
    'Read contents of an open url, use etags and decompress if needed'

    request = Request(url)
    request.add_header('User-Agent', "Raymond's Downloader")
    request.add_header('Accept-Encoding', 'gzip')
    with lock:
        if ('etag ' + url) in cache:
            request.add_header('If-None-Match', cache['etag ' + url])
        if ('mod ' + url) in cache:
            request.add_header('If-Modified-Since', cache['mod ' + url])

    try:
        u = urlopen(request)#, context=no_cert_context)
    except HTTPError as e:
        return Response(e.code, e.msg, False, False)
    content = u.read()
    u.close()

    compressed = get_header(u, 'Content-Encoding') == 'gzip'
    if compressed:
        content = gzip.GzipFile(fileobj=PseudoFile(content), mode='rb').read()

    written = writefile(filename, content) 

    with lock:
        etag = get_header(u, 'Etag')
        if etag:
            cache['etag ' + url] = etag
        timestamp = get_header(u, 'Last-Modified')
        if timestamp:
            cache['mod ' + url] = timestamp

    return Response(u.code, u.msg, compressed, written)



def writefile(filename, content):
    "Only write content if it is not already written."
    try:
        with open(filename, 'rb') as f:
            curr_content = f.read()
            if curr_content == content:
                return False
    except IOError:
        pass
    with open(filename, 'wb') as f:
        f.write(content)
    return True



class Downloader:
    ''' Provides single-argument download method
    that can set a common destination directory for all downloads

        >>> dl = Downloader('foldername')
        >>> result = dl.download('https://www.example.com')
    '''

    def __init__(self, dirname):
        self.dirname = dirname

    def download(self, target):
        'Retrieve a target url and return the download status as a string'
        filename = target.rsplit('/', 1)[-1]
        fullname = os.path.join(self.dirname, filename)
        r = urlretrieve(target, fullname, etags)
        if r.code != 200:
            return '%3d  %-12s %s' % (r.code, r.msg, target)
        compressed = '*' if r.compressed else ' '
        written = '(updated)' if r.written else '(current)'
        fmt = '%3d%1s %-12s %-55s\n                  --> %-25s %s'
        return fmt % (r.code, compressed, r.msg, target, fullname, written)



def parse_args(*args, **kwargs):
    parser = ArgumentParser(description='Download course notes')
    parser.add_argument('destination', default='notes', nargs='?',
                        help='folder name to write files')
    return parser.parse_args(*args, **kwargs)



if __name__ == '__main__':
    args = parse_args()
    try:
        os.mkdir(args.destination)
    except OSError:
        pass

    links_url = links_url_template % class_name
    print((' Source: %s ' % links_url).center(90, '='))
    print((' Starting download at %s ' % time.ctime()).center(90))

    etags = dumbdbm.open(os.path.join(args.destination, 'etag_db'))
    print(links_url)
    links_text = str(urlopen(links_url).read().decode('utf-8'))
    targets = re.findall(r'^https?://\S+', links_text, re.M)

    dl = Downloader(args.destination)
    for line in Pool(25).imap_unordered(dl.download, targets):
        print(line)
    etags.close()
