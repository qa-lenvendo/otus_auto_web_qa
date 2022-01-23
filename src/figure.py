class Figure:

    def __init__(self, name, area, perimetr):
        self.name = name
        self.area = area
        self.perimetr = perimetr

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError('Передан не верный класс')
        else:
            return self.area + figure.area
