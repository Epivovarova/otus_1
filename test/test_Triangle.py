import pytest
from scr.Triangle import Triangle
#импортирую класс треугольник из папки scr и библиотечку pytest

class TestTriangle:

    @pytest.mark.parametrize('ab, bc, ac, expected_perimeter, expected_area', #вот тут использую библиотеку pytest, что бы передать сразу много значений, с которыми будет выполнен тест
                             [ #передаю 3 пары значений сторон треугольника, ожидаемое значение периметра и ожидаемое значение плошади.
                                 (3, 4, 5, 12, 6), #Вверху определял что это такое, а вот тут цифры - соответствующие значения. 3,4,5 - стороны ab,bc,ac, а 12 и 6 - перимтер и плошадь
                                 (5, 5, 8, 18, 12),#при запуске теста функция выполнится с 3 парами значений
                                 (9, 9, 9, 27, 35.1)
                             ])
    def test_positive_creating(self, ab, bc, ac, expected_perimeter, expected_area): #вот тут сама функция, куда я эти значения, определенные выше передаю
        triangle = Triangle(ab, bc, ac) #создаю экземляр класса Triangle, используя значения сторон.
        assert triangle.get_perimeter() == expected_perimeter #сравниваем то, что получилось при вычислении по формуле из класса Triangle с ожидаемым, который мы передали выше
        assert triangle.get_area() == expected_area


    @pytest.mark.parametrize('ab, bc, ac',
                             [
                                 (3, -4, 5), (-5, 5, 8), (9, 9, -9), (-3, -4, -5)
                             ])
    def test_dont_create_negative_side(self, ab, bc, ac): #тут передаю отрицательные значения и смотрю, что мое исключение из класса Triangle работает и свалилась ошибка
        with pytest.raises(ValueError):
            Triangle(ab, bc, ac)

    @pytest.mark.parametrize('ab, bc, ac',
                             [
                                 (0, 4, 5),(5, 0, 8), (9, 9, 0), (0, 0, 0) #аналогично с 0
                             ])
    def test_dont_create_null_side(self, ab, bc, ac):
        with pytest.raises(ValueError):
            Triangle(ab, bc, ac)

    @pytest.mark.parametrize('ab, bc, ac',
                             [
                                (None, 4, 5),(5, None, 8), (9, 9, None), (None, None, None) #аналогично с None. Это я как будто бы не передаю никакое значение вовсе
                              ])
    def test_dont_create_none_side(self, ab, bc, ac):
        with pytest.raises(TypeError):
            Triangle(ab, bc, ac)

    @pytest.mark.parametrize('ab, bc, ac',
                             [
                                ('str', 4, 5),(5, 'str', 8), (9, 9, 'str'),('str', 'int', 'float') #аналогично с неверным форматом данных

                              ])
    def test_dont_create_str_side(self, ab, bc, ac):
        with pytest.raises(TypeError):
            Triangle(ab, bc, ac)