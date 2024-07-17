import unittest
from unittest.mock import patch
from django.test import RequestFactory
from .views import search_weather
from .models import SearchHistory
import ssl

from django.contrib.auth.models import User

class TestSearchWeather(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    @patch('requests.get')
    def test_search_weather_uses_tls1_3_ssl_protocol(self, mock_get):
        request = self.factory.post('/search/', {'city': 'New York'})
        request.user = self.user
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'weather': 'Sunny'}

        search_weather(request)

        mock_get.assert_called_once_with(
            'https://api.openweathermap.org/data/2.5/weather?q=New York&appid=your_api_key',
            ssl_version=ssl.PROTOCOL_TLSv1_3
        )

    @patch('requests.get')
    def test_search_weather_handles_ssl_version_error(self, mock_get):
        request = self.factory.post('/search/', {'city': 'New York'})
        request.user = self.user
        mock_get.side_effect = ssl.SSLError()

        response = search_weather(request)

        self.assertEqual(response.status_code, 500)

    @patch('requests.get')
    def test_search_weather_handles_api_error(self, mock_get):
        request = self.factory.post('/search/', {'city': 'New York'})
        request.user = self.user
        mock_get.return_value.status_code = 404

        response = search_weather(request)

        self.assertEqual(response.status_code, 500)
    @patch('requests.get')
    def test_search_weather_creates_search_history(self, mock_get):
        request = self.factory.post('/search/', {'city': 'New York'})
        request.user = self.user
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'weather': 'Sunny'}

        search_weather(request)

        self.assertEqual(SearchHistory.objects.count(), 1)
        self.assertEqual(SearchHistory.objects.first().city, 'New York')
        self.assertEqual(SearchHistory.objects.first().user, self.user)

if __name__ == '__main__':
    unittest.main()
