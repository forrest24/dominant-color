from django.test import SimpleTestCase
from django.urls import reverse
from rest_framework import status


# TODO: Add more tests
class DominantColorAPITests(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_url = 'http://google.com'
        cls.invalid_url = 'invalid'

    def test_empty_url(self):
        response = self.client.get(reverse('dominant-color'), {'url': ''})
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_url(self):
        response = self.client.get(reverse('dominant-color'), {'url': self.invalid_url})
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
