import pytest
from scr.Circle import Circle



class TestCircle:
    @pytest.mark.parametrize('radius, expected_perimeter, expected_area', [
        (5, 31.4, 78.5),
        (10, 62.8, 314),
        (101, 634.68, 32033.14)
    ])
    def test_get_perimeter_and_area(self, radius, expected_perimeter, expected_area):
        circle = Circle(radius)
        assert circle.get_perimeter() == pytest.approx(expected_perimeter, 0.001)
        assert circle.get_area() == pytest.approx(expected_area, 0.001)

    @pytest.mark.parametrize('radius', [
        -5, -10, -1000
    ])
    def test_dont_create_negative_radius(self, radius):
        with pytest.raises(ValueError):
            Circle(radius)

    @pytest.mark.parametrize('radius', [
        0
    ])
    def test_dont_create_null_radius(self, radius):
        with pytest.raises(ValueError):
            Circle(radius)

    @pytest.mark.parametrize('radius_type', [
        'str',
        None
    ])
    def test_dont_create_none_radius(self, radius_type):
        with pytest.raises((TypeError, ValueError)):
            Circle(radius_type)
