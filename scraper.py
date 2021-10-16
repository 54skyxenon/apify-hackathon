''' scraper.py - Scrapes the webpage data. '''

from typing import List

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

MAX_DELAY_SECS = 4
VIDEO_ENDPOINT = 'https://www.spreadthesign.com/isl.intl/search/'
IMAGE_ENDPOINTS = {
    'English (United States)': 'us',
    'German (Germany)': 'de',
    'Czech': 'cz'
}

class SignLanguageScraper:
    def __init__(self, language: str, word: str) -> None:
        self.language = language
        self.word = word

    def get_video_url(self) -> str:
        ''' Gets a video of our word being read in a specific language. 
            Returns `None` if video translation is unavailable. '''
        
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(VIDEO_ENDPOINT)

        ## search for our word
        search_field = driver.find_element_by_id('search-field')
        search_field.send_keys(self.word)
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

    def get_spelling_images(self) -> List[str]:
        ''' Maps the spelling of a word to a sequence of image URLs. '''
        pass

### Tests
if __name__ == "__main__":
    sl1 = SignLanguageScraper('English (United States)', 'university')
    print(sl1.get_video_url())
    sl2 = SignLanguageScraper('Czech', 'university')
    print(sl2.get_video_url())
    sl3 = SignLanguageScraper('German (Germany)', 'university')
    print(sl3.get_video_url())