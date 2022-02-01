from src.figures.figure import Figure


class Rectangle(Figure):
    def __new__(cls, *args, **kwargs):
        if len(args) != 2:
            return None
        else:
            return super().__new__(cls)

    def __init__(self, *args):
        self.side_a = args[0]
        self.side_b = args[1]
        self.area = self.get_area()
        self.perimetr = self.get_perimetr()
        super().__init__('Rectangle', self.area, self.perimetr)

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimetr(self):
        return 2 * (self.side_a + self.side_b)

    def __repr__(self):
        return f'Name: {self.name} | Side A: {self.side_a} | Side B: {self.side_b} | Area: {self.area} | ' \
               f'Perimetr: {self.perimetr}'

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (
                    self.name == other.name and
                    self.side_a == other.side_a and
                    self.side_b == other.side_b and
                    self.area == other.area and
                    self.perimetr == other.perimetr
            )

        return NotImplemented
