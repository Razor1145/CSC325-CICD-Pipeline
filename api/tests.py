
from django.test import TestCase
from django.urls import reverse


class HelloAPITests(TestCase):

    def test_hello_endpoint_returns_200(self):
        response = self.client.get(reverse('hello_api'))
        self.assertEqual(response.status_code, 200)

    def test_hello_endpoint_returns_correct_message(self):
        response = self.client.get(reverse('hello_api'))
        self.assertEqual(
            response.json()['message'],
            'Hello from CSC325!'
        )

        
    def test_hello_endpoint_returns_version(self):
        response = self.client.get(reverse('hello_api'))
        self.assertEqual(
            response.json()['version'],
            '2.0'
        )

