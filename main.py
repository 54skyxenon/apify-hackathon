''' main.py - Responds with sign language images/video URLs from plaintext input. '''

from apify_client import ApifyClient
from scraper import SignLanguageScraper
import os
import json

### Load actor environment variables
APIFY_TOKEN = os.getenv('APIFY_TOKEN')
APIFY_DEFAULT_KEY_VALUE_STORE_ID = os.getenv('APIFY_DEFAULT_KEY_VALUE_STORE_ID')

### References to the client data
apify_client = ApifyClient(token=APIFY_TOKEN)
kv_store = apify_client.key_value_store(APIFY_DEFAULT_KEY_VALUE_STORE_ID)
json_input_record = kv_store.get_record('INPUT')

### Verify input was received
print('Input received:')
print(json_input_record)

### Verify output being sent is valid
kv_store.set_record('OUTPUT', {'foo': 'bar'})
print('Output sent:')
print(kv_store.get_record('OUTPUT'))