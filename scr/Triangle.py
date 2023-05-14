import math

from scr.Figure import Figure

class Triangle(Figure):

    def __init__(self, ab:int, bc:int, ac:int):
        super().__init__('Triangle')
        self.ab = ab
        self.bc = bc
        self.ac = ac
        if ab + bc <= ac or ab + ac <= bc or ab + ac <= ab:
            raise ValueError("нельзя создать треугольник с заданными значениями сторон")
        if ab <= 0 or bc <= 0 or ac <= 0:
            raise ValueError("Стороны треугольника должны быть больше 0")

    def get_perimeter(self):
        return self.ab + self.bc + self.ac

    def get_area(self) -> float:
        half_per = (self.ab + self.bc + self.ac) / 2
        area = math.sqrt(half_per * (half_per - self.ab) * (half_per - self.bc) * (half_per - self.ac))
        return round(area, 1)
