"""
Тема 15. property и сеттеры
"""


# Задание 1
# Создайте класс CourseProgress.
# В __init__ принимайте student_name и percent.
# Храните процент выполнения во внутреннем атрибуте _percent.
# Добавьте property percent, который возвращает _percent.
# Создайте объект и выведите progress.percent.


# TODO: решение
class CourseProgress:
    def __init__(self, student_name, percent):
        self.student_name = student_name
        self._percent = percent

    @property
    def percent(self):
        return self._percent

progress = CourseProgress("Иван Иванов", 75)
print(progress.percent)

# Задание 2
# Добавьте в CourseProgress сеттер для percent.
# Процент не может быть меньше 0 или больше 100.
# В __init__ используйте self.percent = percent, чтобы начальное значение тоже проходило проверку.


# TODO: решение
class CourseProgress:
    def __init__(self, student_name, percent):
        self.student_name = student_name
        self.percent = percent  # используем сеттер для проверки

    @property
    def percent(self):
        return self._percent

    @percent.setter
    def percent(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Процент должен быть от 0 до 100")
        self._percent = value


progress = CourseProgress("Иван Иванов", 75)
print(progress.percent)

# Задание 3
# Создайте класс Passport.
# В __init__ принимайте number.
# Храните номер во внутреннем атрибуте _number.
# Добавьте property number без сеттера.
# Проверьте, что номер можно прочитать через passport.number.


# TODO: решение
class Passport:
    def __init__(self, number):
        self._number = number

    @property
    def number(self):
        return self._number


passport = Passport("1234 567890")
print(passport.number)

# Задание 4
# Создайте класс Circle.
# В __init__ принимайте radius.
# Добавьте property diameter, который возвращает диаметр.
# Добавьте property area, который возвращает площадь круга.
# Для числа pi можно использовать 3.14.


# TODO: решение
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return 3.14 * self.radius ** 2


circle = Circle(5)
print(circle.diameter)
print(circle.area)

# Задание 5
# Создайте класс StorageBox.
# Внутри храните _items_count.
# Добавьте property items_count только для чтения.
# Добавьте методы add_items(count) и remove_items(count).
# Нельзя добавлять или убирать количество меньше или равное 0.
# Нельзя убрать больше предметов, чем есть в коробке.


# TODO: решение
class StorageBox:
    def __init__(self, initial_count=0):
        self._items_count = initial_count

    @property
    def items_count(self):
        return self._items_count

    def add_items(self, count):
        if count <= 0:
            raise ValueError("Количество для добавления должно быть положительным")
        self._items_count += count

    def remove_items(self, count):
        if count <= 0:
            raise ValueError("Количество для удаления должно быть положительным")
        if count > self._items_count:
            raise ValueError("Нельзя удалить больше предметов, чем есть в коробке")
        self._items_count -= count

# Задание 6
# Создайте класс Speed.
# Внутри храните скорость в километрах в час.
# Добавьте property kmh с сеттером.
# Скорость не может быть отрицательной.
# Добавьте property ms, который возвращает скорость в метрах в секунду по формуле:
# kmh / 3.6


# TODO: решение
class Speed:
    def __init__(self, kmh=0):
        self.kmh = kmh

    @property
    def kmh(self):
        return self._kmh

    @kmh.setter
    def kmh(self, value):
        if value < 0:
            raise ValueError("Скорость не может быть отрицательной")
        self._kmh = value

    @property
    def ms(self):
        return self._kmh / 3.6


speed = Speed(72)
print(speed.kmh)
print(speed.ms)