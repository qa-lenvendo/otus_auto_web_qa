from math import sqrt
from src.figure import Figure


class Triangle(Figure):
    def __new__(cls, *args, **kwargs):
        if len(args) != 3:
            return None
        else:
            return super().__new__(cls)

    def __init__(self, *args):
        self.side_a = args[0]
        self.side_b = args[1]
        self.side_c = args[2]
        self.area = self.get_area()
        self.perimetr = self.get_perimetr()
        super().__init__('Triangle', self.area, self.perimetr)

    def get_area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        area = sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))
        return area

    def get_perimetr(self):
        return self.side_a + self.side_b + self.side_c

    def __repr__(self):
        return f'Name: {self.name} | Side A: {self.side_a} | Side B: {self.side_b} | Side C: {self.side_c} | ' \
               f'Area: {self.area} | Perimetr: {self.perimetr}'

    def __eq__(self, other):
        if isinstance(other, Triangle):
            return (
                    self.name == other.name and
                    self.side_a == other.side_a and
                    self.side_b == other.side_b and
                    self.side_c == other.side_c and
                    self.area == other.area and
                    self.perimetr == other.perimetr
            )

        return NotImplemented
