from src.circle import Circle
from src.rectangle import Rectangle
from src.triangle import Triangle
from src.square import Square
import pytest
from src.yandex_api import YandexApi
from src.jsonplaceholder_helper import JsonPlaceholderHelper
from src.dog_helper import DogHelper
from src.openbrewerydb_helper import OpenBreweryDb


@pytest.fixture(scope='function')
def triangle():
    triangle = Triangle(13, 14, 15)
    yield triangle


@pytest.fixture(scope='function')
def circle():
    circle = Circle(10)
    yield circle


@pytest.fixture(scope='function')
def square():
    square = Square(10)
    yield square


@pytest.fixture(scope='function')
def rectangle():
    rectangle = Rectangle(10, 15)
    yield rectangle


@pytest.fixture(scope='function')
def api_openbrewerydb(request):
    host = request.config.getoption("--openbrewerydb_host")
    data_api = OpenBreweryDb(host=host)

    yield data_api

    data_api.close()


@pytest.fixture(scope='function')
def api_jsonplaceholder(request):
    host = request.config.getoption("--jsonplaceholder_host")
    data_api = JsonPlaceholderHelper(host=host)

    yield data_api

    data_api.close()


@pytest.fixture(scope='function')
def api_dog(request):
    host = request.config.getoption("--api_dog_host")
    data_api = DogHelper(host=host)

    yield data_api

    data_api.close()


@pytest.fixture(scope='function')
def yandex_api(request):
    url = request.config.getoption("--url")
    status_code = request.config.getoption("--status_code")
    data_api = YandexApi(url=url, status_code=status_code)

    yield data_api

    data_api.close()


def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='https://ya.ru', help='input api host')
    parser.addoption('--status_code', action='store', default=200, help='input expect status code')
    parser.addoption('--openbrewerydb_host', action='store', default='https://api.openbrewerydb.org',
                     help='input api host')
    parser.addoption('--jsonplaceholder_host', action='store', default='https://jsonplaceholder.typicode.com',
                     help='input api host')
    parser.addoption('--api_dog_host', action='store', default='https://dog.ceo/api', help='input api host')
