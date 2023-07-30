import os
import time
from collections import defaultdict

import requests
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from PIL import Image


class DominantColorAlgorithm:

    def __init__(self, url):
        self.url = url if url.startswith(('https://', 'http://')) else f'https://{url}'
        self.error = None
        self.file_name = 'current_page.png'

    def _take_screenshot(self):
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--window-size=1920,1080')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(self.url)

            time.sleep(1)  # wait for page to be fully loaded

            driver.save_screenshot(self.file_name)
            driver.quit()
        except WebDriverException:
            self.error = 'Unable to get page screenshot. Check if given URL is valid'

    def _is_black_white_or_grey(self, r, g, b):
        if r == g == b == 255 or r == g == b == 0:
            return True

        avg_diff = abs(r - g) + abs(g - b) + abs(b - r)
        if avg_diff < 20:
            return True

        return False

    def _cleanup(self):
        os.remove(self.file_name)

    def _get_dominant(self):
        image = Image.open(self.file_name)

        colors = defaultdict(int)
        for r, g, b, _ in image.getdata():
            if not self._is_black_white_or_grey(r, g, b):
                colors[(r, g, b)] += 1

        ordered_colors = {k: v for k, v in sorted(colors.items(), key=lambda item: item[1], reverse=True)}
        if len(ordered_colors) > 0:
            dominant_color_rgb = list(ordered_colors.keys())[0]
            response = requests.get(f'http://www.thecolorapi.com/id?rgb=rgb{dominant_color_rgb}').json()
            return dominant_color_rgb, response['name']['value']

        return None, None

    def get_dominant_color(self):
        self._take_screenshot()
        if self.error:
            return None, None, self.error

        rgb, name = self._get_dominant()

        self._cleanup()

        return rgb, name, self.error
