"""
Тема 8. Функции
"""


# Задание 1
# Напишите функцию greet(name), которая выводит:
# Привет, <name>!
# Вызовите функцию три раза с разными именами.


# TODO: решение
def greet(name):
    print(f"Привет, {name}")

greet("Anna")
greet("Ivan")
greet("Maria")

# Задание 2
# Напишите функцию add(a, b), которая возвращает сумму двух чисел.
# Вызовите функцию и выведите результат.


# TODO: решение
def add(a, b):
    return a + b

result = add(3, 5)
print(result)

# Задание 3
# Напишите функцию is_even(number), которая возвращает True,
# если число четное, и False, если нечетное.
# Проверьте функцию на нескольких числах.


# TODO: решение
def is_even(number):
    return number % 2 == 0

print(is_even(4))
print(is_even(7))
print(is_even(10))

# Задание 4
# Напишите функцию get_max(a, b, c), которая возвращает наибольшее
# из трех чисел.


# TODO: решение
def get_max(a, b, c):
    return max(a, b, c)

print(get_max(5, 9, 3))

# Задание 5
# Напишите функцию count_vowels(text), которая считает количество
# гласных букв в строке.
# Можно считать гласными: a, e, i, o, u, y.


# TODO: решение
def count_flowers(text):
    vowels = "aeiouy"
    count = 0
    for char in text:
        if char in vowels:
            count = count + 1
    return count

print(count_flowers("hello world"))
print(count_flowers("python"))

# Задание 6
# Напишите функцию calculate_total(price, count, discount=0).
# Функция должна возвращать итоговую стоимость:
# price * count минус скидка в процентах.
# Пример: price=100, count=3, discount=10 -> 270.


# TODO: решение
def calculate_total(price, count, discount=0):
    total = price * count
    discount_amount = total * discount / 100
    return total - discount_amount

print(calculate_total(100, 3, 10))
print(calculate_total(50, 2))