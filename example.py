#!/usr/bin/env python3

from apify_client import ApifyClient
import urllib.request as u2
from lxml import html
import os, json

API_TOKEN = os.getenv('APIFY_TOKEN')
APIFY_DEFAULT_KEY_VALUE_STORE_ID = os.getenv('APIFY_DEFAULT_KEY_VALUE_STORE_ID')

apify_client = ApifyClient(token=API_TOKEN)
kv_store = apify_client.key_value_store(APIFY_DEFAULT_KEY_VALUE_STORE_ID)
json_record = kv_store.get_record('INPUT')

print('Input received:')
print(json_record)

request = u2.Request('https://example.com/')
src = u2.urlopen(request).read()
html_load = html.fromstring(src.decode())
print( html_load.xpath('//h1/text()')[0] )