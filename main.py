''' main.py - Responds with sign language images/video URLs from plaintext input. '''

from apify_client import ApifyClient
from scraper import SignLanguageScraper
import os

### Load actor environment variables
APIFY_TOKEN = os.getenv('APIFY_TOKEN')
APIFY_DEFAULT_KEY_VALUE_STORE_ID = os.getenv('APIFY_DEFAULT_KEY_VALUE_STORE_ID')

### References to the client data
apify_client = ApifyClient(token=APIFY_TOKEN)
kv_store = apify_client.key_value_store(APIFY_DEFAULT_KEY_VALUE_STORE_ID)
json_input_record = kv_store.get_record('INPUT')['value']

### Verify input was received
print('Input received:')
print(str(type(json_input_record)) + ': ' + str(json_input_record))

### Call the sign language scraper
scraper = SignLanguageScraper(json_input_record['language'], json_input_record['word'])

### Add the video url and image urls to output key store
kv_store.set_record('OUTPUT', {'video_url': scraper.get_video_url(), 'image_urls': scraper.get_spelling_images()})

### Verify output being sent is valid
print('Output sent:')
print(kv_store.get_record('OUTPUT'))