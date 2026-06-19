"""
Тема 13. Атрибуты класса и атрибуты объекта
"""


# Задание 1
# Создайте класс Course.
# У класса должен быть атрибут класса platform со значением "Stepik".
# В __init__ сохраните title как атрибут объекта.
# Создайте два курса и выведите их названия и platform.


# TODO: решение
class Course:
    platform = "Stepik"

    def __init__(self, title):
        self.title = title

course1 = Course("Python для начинающих")
course2 = Course("ООП на практике")

print(course1.title, course1.platform)
print(course2.title, course2.platform)

# Задание 2
# Создайте класс Ticket.
# У класса должен быть атрибут класса currency со значением "руб.".
# В __init__ сохраните event_name и price.
# Добавьте метод get_info(), который возвращает строку:
# Билет на <event_name>: <price> <currency>


# TODO: решение
class Ticket:
    currency = "руб."

    def __init__(self, event_name, price):
        self.event_name = event_name
        self.price = price

    def get_info(self):
        return f"Билет на {self.event_name}: {self.price} {self.currency}"

# Задание 3
# Создайте класс Visit.
# Добавьте атрибут класса total_visits со значением 0.
# При создании каждого объекта увеличивайте Visit.total_visits на 1.
# Создайте несколько посещений и выведите Visit.total_visits.


# TODO: решение
class Visit:
    total_visits = 0

    def __init__(self):
        Visit.total_visits += 1

visit1 = Visit()
visit2 = Visit()
visit3 = Visit()

print(Visit.total_visits)

# Задание 4
# Создайте класс Delivery.
# Добавьте атрибуты класса STATUS_WAITING = "waiting" и STATUS_SENT = "sent".
# При создании доставки status должен быть STATUS_WAITING.
# Добавьте метод send(), который меняет status на STATUS_SENT.


# TODO: решение
class Delivery:
    STATUS_WAITING = "waiting"
    STATUS_SENT = "sent"

    def __init__(self):
        self.status = Delivery.STATUS_WAITING

    def send(self):
        self.status = Delivery.STATUS_SENT

# Задание 5
# Создайте класс Laptop.
# У класса должен быть атрибут класса warranty_months.
# У объекта должны быть model и owner.
# Создайте несколько ноутбуков и покажите, что warranty_months общий для всех.


# TODO: решение
class Laptop:
    warranty_months = 24

    def __init__(self, model, owner):
        self.model = model
        self.owner = owner

laptop1 = Laptop("Dell XPS", "Анна")
laptop2 = Laptop("MacBook Pro", "Иван")
print(Laptop.warranty_months)


# Задание 6
# Создайте класс Message.
# У класса должен быть атрибут total_sent.
# Каждый новый объект увеличивает total_sent.
# Добавьте метод get_total_sent(), который возвращает общее количество созданных сообщений.


# TODO: решение
class Message:
    total_sent = 0

    def __init__(self):
        Message.total_sent += 1

    def get_total_sent(self):
        return Message.total_sent

msg1 = Message()
msg2 = Message()
msg3 = Message()

print(msg3.get_total_sent())  