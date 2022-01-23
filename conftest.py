import pytest
from src.circle import Circle
from src.rectangle import Rectangle
from src.triangle import Triangle
from src.square import Square


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
