import pytest
from scr.Square import Square


class TestSquare:

    @pytest.mark.parametrize('side, expected_perimeter, expected_area',
                             [
                                 (10, 40, 100),
                                 (1, 4, 1),
                                 (999, 3996, 998001)
                             ])
    def test_positive_creating(self, side, expected_perimeter, expected_area):
        square = Square(side)
        assert square.get_perimeter() == expected_perimeter
        assert square.get_area() == expected_area

    @pytest.mark.parametrize('side',
                             [
                                 (-3), (-10), (-1000)
                             ])
    def test_dont_create_negative_side(self, side):
        with pytest.raises(ValueError):
            Square(side)

    @pytest.mark.parametrize('side',
                             [
                                 (0)
                             ])
    def test_dont_create_null_side(self, side):
        with pytest.raises(ValueError):
            Square(side)

    @pytest.mark.parametrize('side',
                             [
                                ('str')
                              ])
    def test_dont_create_str_side(self, side):
        with pytest.raises(TypeError):
            Square(side)

    @pytest.mark.parametrize('side', [
        (None)
    ])
    def test_dont_create_none_side(self, side):
        with pytest.raises(TypeError):
            Square(side)