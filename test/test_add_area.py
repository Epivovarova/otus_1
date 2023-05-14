import pytest
from scr.Circle import Circle
from scr.Rectangle import Rectangle
from scr.Square import Square
from scr.Triangle import Triangle


class TestAddArea:

    @pytest.fixture
    def rectangle(self):
        return Rectangle(5, 10)

    @pytest.fixture
    def square(self):
        return Square(4)

    @pytest.fixture
    def circle(self):
        return Circle(10)

    @pytest.fixture
    def triangle(self):
        return Triangle(3, 4, 5)

    def test_add_area_rectangle_square(self, rectangle, square):
        assert rectangle.add_area(square) == 66

    def test_add_area_square_circle(self, square, circle):
        assert square.add_area(circle) == 330

    def test_add_area_circle_triangle(self, circle, triangle):
        assert circle.add_area(triangle) == 320

