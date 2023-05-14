from scr.Figure import Figure


class Circle(Figure):
    def __init__(self, radius: int):
        super().__init__('Circle')
        self.radius = radius
        if radius <= 0:
            raise ValueError('Радиус круга должен больше 0')


    def get_perimeter(self):
        return 2 * 3.14 * self.radius

    def get_area(self):
        return 3.14 * self.radius ** 2
