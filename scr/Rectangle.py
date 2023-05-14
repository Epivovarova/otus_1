from scr.Figure import Figure

class Rectangle(Figure):
    def __init__(self, height: int, width: int):
        super().__init__('Rectangle')
        if height <= 0 or width <= 0:
            raise ValueError("Стороны прямоугольника должны быть больше 0")
        self.height = height
        self.width = width

    def get_perimeter(self):
        return (self.height + self.width) * 2

    def get_area(self):
        return self.height * self.width
