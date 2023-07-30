from unittest.mock import patch

from django.test import SimpleTestCase
from selenium.common.exceptions import WebDriverException

from apps.colors.dominant_color_algorithm import DominantColorAlgorithm


# TODO: Add more tests
class DominantColor(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_url = 'http://google.com'
        cls.invalid_url = 'invalid'

    @patch('apps.colors.dominant_color_algorithm.webdriver.Chrome.get')
    def test_take_screenshot_invalid_url(self, driver_mock):
        driver_mock.side_effect = WebDriverException
        algorithm = DominantColorAlgorithm(self.invalid_url)
        _, _, error = algorithm.get_dominant_color()
        self.assertEquals(error, 'Unable to get page screenshot. Check if given URL is valid')
