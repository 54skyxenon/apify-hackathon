#!/usr/bin/env python3

from apify_client import ApifyClient
import os
import json

API_TOKEN = os.getenv('APIFY_TOKEN')
APIFY_DEFAULT_KEY_VALUE_STORE_ID = os.getenv('APIFY_DEFAULT_KEY_VALUE_STORE_ID')
APIFY_DEFAULT_DATASET_ID = os.getenv('APIFY_DEFAULT_DATASET_ID')

apify_client = ApifyClient(token=API_TOKEN)
kv_store = apify_client.key_value_store(APIFY_DEFAULT_KEY_VALUE_STORE_ID)
dataset = apify_client.dataset(APIFY_DEFAULT_DATASET_ID)
json_input_record = kv_store.get_record('INPUT')

print('Input received:')
print(json_input_record)

print('Dataset')
dataset.push_items({'foo': 'bar'})
print(dataset.download_items().decode())