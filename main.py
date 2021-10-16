''' main.py - Responds with sign language images/video URLs from plaintext input. '''

from apify_client import ApifyClient
from scraper import SignLanguageScraper
import os
import base64
import json

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

letter_images_base64 = []

### TODO: implement get spelling images
# for letter_file_path in scraper.get_spelling_images():
#     with open(letter_file_path, "rb") as image_file:
#         encoded_letter_image = base64.b64encode(image_file.read())
#         images_base64.append(encoded_letter_image)

kv_store.set_record('OUTPUT', {'video_url': scraper.get_video_url(), 'images_base64': letter_images_base64})

### Verify output being sent is valid
print('Output sent:')
print(kv_store.get_record('OUTPUT'))