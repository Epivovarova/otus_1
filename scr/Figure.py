class Figure:
    def __init__(self, name):
        self.name = name

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return round(self.get_area() + figure.get_area(), 2)
        raise ValueError(f'Object {figure} is not subclass of Figure class')

#print(dir(Figure))
print(Figure)
circle = Figure("circle")
print(circle)


