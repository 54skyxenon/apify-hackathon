#!/usr/bin/env python3

from apify_client import ApifyClient
import urllib.request as u2
from lxml import html
import os, json

print('HELLO WORLD!')
request = u2.Request('https://example.com/')
src = u2.urlopen(request).read()
html_load = html.fromstring( src.decode() )
print( html_load.xpath('//h1/text()')[0] )