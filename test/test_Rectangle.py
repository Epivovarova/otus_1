import pytest
from scr.Rectangle import Rectangle


class TestRectangle:

    @pytest.mark.parametrize('height, width, expected_perimeter, expected_area',
                             [
                                 (3, 4, 14, 12),
                                 (5, 7, 24, 35),
                                 (9, 12, 42, 108),
                             ])
    def test_positive_creating(self, height, width, expected_perimeter, expected_area):
        rect = Rectangle(height, width)
        assert rect.get_perimeter() == expected_perimeter
        assert rect.get_area() == expected_area

    @pytest.mark.parametrize('height, width',
                             [
                                 (-3, 4), (5, -7), (-9, -12), (-3, -10)
                             ])
    def test_dont_create_negative_side(self, height, width):
        with pytest.raises(ValueError):
            Rectangle(height, width)

    @pytest.mark.parametrize('height, width',
                             [
                                 (0, 4), (5, 0), (0, 0)
                             ])
    def test_dont_create_null_side(self, height, width):
        with pytest.raises(ValueError):
            Rectangle(height, width)

    @pytest.mark.parametrize('height, width',
                             [
                                ('str', 4), (5, 'str'), ('str', 'string')
                              ])
    def test_dont_create_str_side(self, height, width):
        with pytest.raises(TypeError):
            Rectangle(height, width)

    @pytest.mark.parametrize('height, width', [
        (None, 4),
        (55, None),
        (None, None)
    ])
    def test_dont_create_none_side(self, height, width):
        with pytest.raises(TypeError):
            Rectangle(height, width)