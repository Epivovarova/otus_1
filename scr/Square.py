from scr.Figure import Figure


class Square(Figure):
    def __init__(self, side: int):
        super().__init__('Square')
        self.side = side
        if side <= 0:
            raise ValueError('Сторона квадрата должна быть больше 0')

    def get_perimeter(self):
        return self.side * 4

    def get_area(self):
        return self.side ** 2


