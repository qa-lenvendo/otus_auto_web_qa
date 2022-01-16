from math import pi
from src.figure import Figure


class Circle(Figure):
    def __new__(cls, *args, **kwargs):
        if len(args) != 1:
            return None
        else:
            return super().__new__(cls)

    def __init__(self, *args):
        self.radius = args[0]
        self.area = self.get_area()
        self.perimetr = self.get_perimetr()
        super().__init__('Circle', self.area, self.perimetr)

    def get_area(self):
        return pi * self.radius ** 2

    def get_perimetr(self):
        return 2 * pi * self.radius

    def __repr__(self):
        return f'Name: {self.name} | Radius: {self.radius} | Area: {self.area} | Perimetr: {self.perimetr}'

    def __eq__(self, other):
        if isinstance(other, Circle):
            return (
                self.name == other.name and
                self.radius == other.radius and
                self.area == other.area and
                self.perimetr == other.perimetr
            )

        return NotImplemented
