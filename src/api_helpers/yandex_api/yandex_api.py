import requests


class YandexApi:
    def __init__(self, url, status_code):
        self.url = url
        self.status_code = status_code
        self.request = requests.Session()

    def test_status_code(self):
        response = self.request.get(url=self.url)
        assert response.status_code == int(self.status_code), f'{response.status_code}'

    def close(self):
        self.request.close()
