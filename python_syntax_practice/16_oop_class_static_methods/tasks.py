"""
Тема 16. classmethod и staticmethod
"""


# Задание 1
# Создайте класс Employee с атрибутами name и position.
# Добавьте обычный метод get_info(), который возвращает строку с именем и должностью.


# TODO: решение
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} - {self.position}"

# Задание 2
# Добавьте в Employee метод класса from_dict(data).
# Он должен создавать сотрудника из словаря:
# {"name": ..., "position": ...}


# TODO: решение
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} - {self.position}"

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["position"])

# Задание 3
# Создайте класс Song с атрибутами title и duration.
# Добавьте метод класса from_string(text).
# Строка приходит в формате:
# title;duration
# Например: "Imagine;183"


# TODO: решение
class Song:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    @classmethod
    def from_string(cls, text):
        title, duration = text.split(";")
        return cls(title, int(duration))



# Задание 4
# Создайте класс TextHelper.
# Добавьте staticmethod is_short(text), который возвращает True,
# если длина строки меньше 10, и False иначе.
# Проверьте метод без создания объекта.


# TODO: решение
class TextHelper:
    @staticmethod
    def is_short(text):



        
        return len(text) < 10

# Задание 5
# Создайте класс Password.
# В __init__ принимайте value.
# Добавьте staticmethod is_strong(value), который проверяет,
# что длина пароля не меньше 8.
# Если пароль слишком короткий, выбрасывайте ValueError.



# TODO: решение
class Password:
    def __init__(self, value):
        self.is_strong(value)  # проверяем при создании
        self.value = value

    @staticmethod
    def is_strong(value):
        if len(value) < 8:
            raise ValueError("Пароль слишком короткий. Должен быть не менее 8 символов.")

# Задание 6
# Создайте класс Time.
# В __init__ принимайте hours и minutes.
# Добавьте classmethod from_string(text).
# Строка приходит в формате:
# "09:30"
# Метод должен вернуть объект Time.
# Добавьте __str__(), чтобы время красиво выводилось через print().


# TODO: решение
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    @classmethod
    def from_string(cls, text):
        hours, minutes = map(int, text.split(":"))
        return cls(hours, minutes)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"