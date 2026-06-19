"""
Тема 9. Основы ООП: классы и объекты
"""


# Задание 1
# Создайте класс Student.
# В __init__ сохраните name и age.
# Создайте объект и выведите его имя и возраст.


# TODO: решение
class Student:
    def __init__(self, name, faculty):
        self.name = name
        self.faculty = faculty

student = Student("Anna", "Информатика")
print(student.name)
print(student.faculty)

# Задание 2
# Добавьте в класс Student метод greet().
# Метод должен возвращать строку:
# Привет, меня зовут <name>.


# TODO: решение
class Student:
    def __init__(self, name, faculty):
        self.name = name
        self.faculty = faculty

    def greet(self):
        return f"Привет, меня зовут {self.name}."

student = Student("Anna", "Информатика")
print(student.greet())

# Задание 3
# Создайте класс Product с атрибутами title и price.
# Добавьте метод get_info(), который возвращает строку:
# <title>: <price> руб.


# TODO: решение
class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def get_info(self):
        return f"{self.title}: {self.price} руб."

product = Product("Хлеб", 50)
print(product.get_info())

# Задание 4
# Создайте класс Rectangle с атрибутами width и height.
# Добавьте метод area(), который возвращает площадь.
# Добавьте метод perimeter(), который возвращает периметр.


# TODO: решение
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print(rect.area())
print(rect.perimeter())

# Задание 5
# Создайте класс BankAccount.
# Внутри храните owner и balance.
# Добавьте методы deposit(amount) и withdraw(amount).
# deposit увеличивает баланс.
# withdraw уменьшает баланс, если денег достаточно.


# TODO: решение
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def get_balance(self):
        return self.balance

account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print(account.get_balance())

# Задание 6
# Создайте несколько объектов Student и положите их в список.
# С помощью цикла выведите информацию о каждом студенте.


# TODO: решение
class Student:
    def __init__(self, name, faculty):
        self.name = name
        self.faculty = faculty

    def get_info(self):
        return f"{self.name}, {self.faculty}"

students = [
    Student("Anna", "Информатика"),
    Student("Ivan", "Математика"),
    Student("Maria", "Физика")
]

for student in students:
    print(student.get_info())