from src.figure import Figure


class Square(Figure):
    def __new__(cls, *args, **kwargs):
        if len(args) != 1:
            return None
        else:
            return super().__new__(cls)

    def __init__(self, *args):
        self.side = args[0]
        self.area = self.get_area()
        self.perimetr = self.get_perimetr()
        super().__init__('Square', self.area, self.perimetr)

    def get_area(self):
        return self.side * self.side

    def get_perimetr(self):
        return self.side * 4

    def __repr__(self):
        return f'Name: {self.name} | Side: {self.side} | Area: {self.area} Perimetr: {self.perimetr}'

    def __eq__(self, other):
        if isinstance(other, Square):
            return (
                    self.name == other.name and
                    self.side == other.side and
                    self.area == other.area and
                    self.perimetr == other.perimetr
            )

        return NotImplemented
