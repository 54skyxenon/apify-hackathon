''' scraper.py - Scrapes the webpage data. '''

from googletrans import Translator

from typing import List

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

MAX_DELAY_SECS = 4
VIDEO_ENDPOINT = 'https://www.spreadthesign.com/isl.intl/search/'

GITHUB_USERNAME = '54skyxenon'
REPO_NAME = 'apify-hackathon'
BRANCH_NAME = 'main'
REMOTE_IMAGE_BASE_URL = f'https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/{BRANCH_NAME}/'

CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument('--headless')
CHROME_OPTIONS.add_argument('--no-sandbox')
CHROME_OPTIONS.add_argument('--disable-dev-shm-usage')

LANG_CODES = {'English (United States)': 'en', 'Czech': 'cs', 'German (Germany)': 'de'}

class SignLanguageScraper:
    ''' Scraper API class. '''

    def __init__(self, language: str, word: str) -> None:
        self.language = language
        self.word = word
        self.translator = Translator()

    def get_video_url(self) -> str:
        ''' Gets a video of our word being read in a specific language. 
            Returns `None` if video translation is unavailable. '''
        
        driver = webdriver.Chrome(
            ChromeDriverManager(log_level=0, print_first_line=False).install(),
            options=CHROME_OPTIONS)

        driver.get(VIDEO_ENDPOINT)

        ## convert our word to search in English
        translation = self.translator.translate(self.word, src=LANG_CODES[self.language], dest=LANG_CODES['English (United States)'])

        ## search for our word
        search_field = driver.find_element_by_id('search-field')
        search_field.send_keys(translation.text)
        search_field.submit()

        ## click language for video URL, then retrieve video mp4 URL
        video_url = None
        try:
            language_tag = WebDriverWait(driver, MAX_DELAY_SECS).until(
                EC.presence_of_element_located((By.XPATH, f"//a[@title='{self.language}']")))
            word_url = language_tag.get_attribute('href')

            driver.get(word_url)
            video_tag = WebDriverWait(driver, MAX_DELAY_SECS).until(
                EC.presence_of_element_located((By.TAG_NAME, 'video')))
            video_url = video_tag.get_attribute('src')
        except TimeoutException:
            pass
        
        driver.quit()
        return video_url

    def get_spelling_image_urls(self) -> List[str]:
        ''' Maps the spelling of a word to a sequence of image URLs. '''
        if self.language == 'English (United States)':
            return self._american_spelling()
        elif self.language == 'German (Germany)':
            return self._german_spelling()
        elif self.language == 'Czech':
            return self._czech_spelling()
        else:
            return []

    def _american_spelling(self) -> List[str]:
        ''' Retrieves US sign language spelling of word. '''
        image_paths = []

        for letter in self.word.lower():
            if letter:
                image_paths.append(REMOTE_IMAGE_BASE_URL + f'assets/us/{letter}.png')

        return image_paths

    def _german_spelling(self) -> List[str]:
        ''' Retrieves German sign language spelling of word. '''
        image_paths = []
        transformed = self.word.lower().replace('sch', '^')
        
        for letter in transformed:
            if letter:
                image_paths.append(REMOTE_IMAGE_BASE_URL + f'assets/de/{letter}.png')

        return image_paths

    def _czech_spelling(self) -> List[str]:
        ''' Retrieves Czech sign language spelling of word. '''
        image_paths = []
        
        ## detect length marked + hooked characters in Czech alphabet
        ## ??, ??, ??, ??, ??, ??, ??, ??, ??, ??, ??, ??, ??, ??, ??
        length_marks = {'??': 'a', '??': 'e', '??': 'i', '??': 'o', '??': 'u', '??': 'u', '??': 'y'}
        hooks = {'??': 'c', '??': 'd', '??': 'e', '??': 'n', '??': 'r', '??': 's', '??': 't', '??': 'z'}

        transformed = self.word.lower().replace('ch', '^')

        for letter in transformed:
            if letter:
                if letter in length_marks:
                    image_paths.append(REMOTE_IMAGE_BASE_URL + f'assets/cz/{length_marks[letter]}.png')
                    image_paths.append(REMOTE_IMAGE_BASE_URL + 'assets/cz/length-mark.png')
                elif letter in hooks:
                    image_paths.append(REMOTE_IMAGE_BASE_URL + f'assets/cz/{hooks[letter]}.png')
                    image_paths.append(REMOTE_IMAGE_BASE_URL + 'assets/cz/hook.png')
                else:
                    image_paths.append(REMOTE_IMAGE_BASE_URL + f'assets/cz/{letter}.png')

        return image_paths

### Tests
if __name__ == "__main__":
    sl1 = SignLanguageScraper('English (United States)', 'university')
    print(sl1.get_video_url())
    print(sl1.get_spelling_image_urls())

    sl2 = SignLanguageScraper('Czech', 'university')
    print(sl2.get_video_url())
    print(sl2.get_spelling_image_urls())

    sl3 = SignLanguageScraper('German (Germany)', 'university')
    print(sl3.get_video_url())
    print(sl3.get_spelling_image_urls())