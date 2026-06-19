"""
Тема 10. Классы-модели
"""


# Задание 1
# Создайте модель User.
# Атрибуты: name, email, age.
# Добавьте метод get_info(), который возвращает строку с данными пользователя.


# TODO: решение
class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def get_info(self):
        return f"{self.name}, {self.email}, {self.age}"

user = User("Anna", "anna@mail.ru", 20)
print(user.get_info())

# Задание 2
# Добавьте в User валидацию возраста.
# Если age меньше 0, выбрасывайте ValueError.


# TODO: решение
class User:
    def __init__(self, name, email, age):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.name = name
        self.email = email
        self.age = age

    def get_info(self):
        return f"{self.name}, {self.email}, {self.age}"

user = User("Anna", "anna@mail.ru", 20)
print(user.get_info())

# Задание 3
# Создайте модель Product.
# Атрибуты: title, price, count.
# Добавьте метод get_total_price(), который возвращает price * count.
# Добавьте проверку: price и count не могут быть отрицательными.


# TODO: решение
class Product:
    def __init__(self, title, price, count):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if count < 0:
            raise ValueError("Количество не может быть отрицательным")
        self.title = title
        self.price = price
        self.count = count

    def get_total_price(self):
        return self.price * self.count

product = Product("Book", 500, 3)
print(product.get_total_price())

# Задание 4
# Создайте модель Task.
# Атрибуты: title, is_done.
# При создании is_done должен быть False.
# Добавьте методы mark_done() и mark_undone().


# TODO: решение
class Task:
    def __init__(self, title):
        self.title = title
        self.is_done = False

    def mark_done(self):
        self.is_done = True

    def mark_undone(self):
        self.is_done = False

task = Task("Купить молоко")
print(task.is_done)
task.mark_done()
print(task.is_done)
task.mark_undone()
print(task.is_done)

# Задание 5
# Добавьте в Task метод to_dict().
# Он должен возвращать словарь:
# {"title": ..., "is_done": ...}


# TODO: решение
class Task:
    def __init__(self, title):
        self.title = title
        self.is_done = False

    def mark_done(self):
        self.is_done = True

    def mark_undone(self):
        self.is_done = False

    def to_dict(self):
        return {
            "title": self.title,
            "is_done": self.is_done
        }

task = Task("Купить молоко")
print(task.to_dict())

# Задание 6
# Создайте модель Order.
# Атрибуты: customer_name, products.
# products — список объектов Product.
# Добавьте метод get_total(), который возвращает сумму всех товаров.


# TODO: решение
class Product:
    def __init__(self, title, price, count):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if count < 0:
            raise ValueError("Количество не может быть отрицательным")
        self.title = title
        self.price = price
        self.count = count

    def get_total_price(self):
        return self.price * self.count

class Order:
    def __init__(self, customer_name, products):
        self.customer_name = customer_name
        self.products = products

    def get_total(self):
        total = 0
        for product in self.products:
            total = total + product.get_total_price()
        return total

product1 = Product("Книга", 500, 2)
product2 = Product("Ручка", 50, 3)
order = Order("Анна", [product1, product2])
print(order.get_total())