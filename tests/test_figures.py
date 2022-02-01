from math import sqrt, pi
from src.figures.triangle import Triangle
from src.figures.square import Square
from src.figures.circle import Circle
from src.figures.rectangle import Rectangle


class TestTriangle:
    """
    Тесты для проверки объекта "Треугольник"
    """

    def test_create_triangle(self, triangle):
        """
        Проверка создания объекта "Треугольник"
        """
        assert isinstance(triangle, Triangle), 'Созданный объект не является треугольником'

    def test_not_create_triangle(self):
        """
        Проверка невозможности создания объекта треугольник при передаче невалидных значений
        """
        triangle = Triangle(10)
        assert triangle is None, 'При передаче невалидных значений был создан объект "Треугольник"'

    def test_triangle_area(self, triangle):
        """
        Проверка корректности вычисления площади треугольника
        """
        triangle_p = (triangle.side_a + triangle.side_b + triangle.side_c) / 2
        expected_area = sqrt(triangle_p * (triangle_p - triangle.side_a) * (triangle_p - triangle.side_b) *
                             (triangle_p - triangle.side_c))

        assert triangle.area == expected_area, f'Площадь треугольника вычислена неверно. ОР: {expected_area}'

    def test_triangle_perimetr(self, triangle):
        """
        Проверка корректности вычисления периметра треугольника
        """
        expected_perimetr = triangle.side_a + triangle.side_b + triangle.side_c

        assert triangle.perimetr == expected_perimetr, f'Периметр треугольника вычислен не верно. ' \
                                                       f'ОР: {expected_perimetr}'

    def test_perimetr_sum_triangle_and_square(self, triangle, square):
        """
        Проверка корректности вычисления суммы периметров треугольника и квадрата
        """
        area_sum = triangle.add_area(square)
        expected_area_sum = triangle.area + square.area

        assert area_sum == expected_area_sum, f'Сумма площадей треугольника и квадрата рассчитана не верно. ' \
                                              f'ОР: {expected_area_sum}'


class TestSquare:
    """
    Тесты для проверки объекта "Квадрат"
    """
    def test_create_square(self, square):
        """
        Проверка создания объекта "Квадрат"
        """
        assert isinstance(square, Square), 'Созданный объект не является квадратом'

    def test_not_create_square(self):
        """
        Проверка невозможности создания объекта квадрат при передаче невалидных значений
        """
        square = Square(10, 15)
        assert square is None, 'При передаче невалидных значений был создан объект "Квадрат"'

    def test_square_area(self, square):
        """
        Проверка корректности вычисления площади квадрата
        """
        expected_area = square.side * square.side

        assert square.area == expected_area, f'Площадь квадрата вычислена неверно. ОР: {expected_area}'

    def test_square_perimetr(self, square):
        """
        Проверка корректности вычисления периметра квадрата
        """
        expected_perimetr = square.side * 4

        assert square.perimetr == expected_perimetr, f'Периметр квадрата вычислен не верно. ' \
                                                     f'ОР: {expected_perimetr}'


class TestRectangle:
    """
    Тесты для проверки объекта "Прямоугольник"
    """
    def test_create_rectangle(self, rectangle):
        """
        Проверка создания объекта "Прямоугольник"
        """
        assert isinstance(rectangle, Rectangle), 'Созданный объект не является квадратом'

    def test_not_create_rectangle(self):
        """
        Проверка невозможности создания объекта прямоугольник при передаче невалидных значений
        """
        rectangle = Rectangle(10)
        assert rectangle is None, 'При передаче невалидных значений был создан объект "Прямоугольник"'

    def test_rectangle_area(self, rectangle):
        """
        Проверка корректности вычисления площади прямоугольника
        """
        expected_area = rectangle.side_a * rectangle.side_b

        assert rectangle.area == expected_area, f'Площадь прямоугольника вычислена неверно. ОР: {expected_area}'

    def test_rectangle_perimetr(self, rectangle):
        """
        Проверка корректности вычисления периметра квадрата
        """
        expected_perimetr = 2 * (rectangle.side_a + rectangle.side_b)

        assert rectangle.perimetr == expected_perimetr, f'Периметр прямоугольника вычислен не верно. '\
                                                        f'ОР: {expected_perimetr}'


class TestCircle:
    """
    Тесты для проверки объекта "Круг"
    """
    def test_create_circle(self, circle):
        """
        Проверка создания объекта "Круг"
        """
        assert isinstance(circle, Circle), 'Созданный объект не является кругом'

    def test_not_create_circle(self):
        """
        Проверка невозможности создания объекта круг при передаче невалидных значений
        """
        circle = Circle(10, 10)
        assert circle is None, 'При передаче невалидных значений был создан объект "Круг"'

    def test_circle_area(self, circle):
        """
        Проверка корректности вычисления площади круга
        """
        expected_area = pi * circle.radius ** 2

        assert circle.area == expected_area, f'Площадь круга вычислена неверно. ОР: {expected_area}'

    def test_circle_perimetr(self, circle):
        """
        Проверка корректности вычисления периметра круга
        """
        expected_perimetr = 2 * pi * circle.radius

        assert circle.perimetr == expected_perimetr, f'Периметр круга вычислен не верно. '\
                                                     f'ОР: {expected_perimetr}'
