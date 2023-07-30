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

    def take_screenshot(self):
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--window-size=1920,1080')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(self.url)

            time.sleep(1)

            driver.save_screenshot('current.png')
            driver.quit()
        except WebDriverException:
            return False

        return True

    def get_dominant(self):
        image = Image.open('current.png')

        colors = defaultdict(int)
        for rgb in image.getdata():
            if abs(rgb[0] - rgb[1]) < 10 or abs(rgb[1] - rgb[2]) < 10:
                continue
            colors[(rgb[0], rgb[1], rgb[2])] += 1

        ordered_colors = {k: v for k, v in sorted(colors.items(), key=lambda item: item[1], reverse=True)}
        if len(ordered_colors) == 0:
            return False, False
        dominant_color_rgb = list(ordered_colors.keys())[0]

        response = requests.get(f'http://www.thecolorapi.com/id?rgb=rgb{dominant_color_rgb}').json()

        os.remove('current.png')

        return dominant_color_rgb, response['name']['value']

    def get_dominant_color(self):
        result = self.take_screenshot()
        if not result:
            return False

        return self.get_dominant()
