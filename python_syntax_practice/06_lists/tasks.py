"""
Тема 6. Списки
"""


# Задание 1
# Создайте список из пяти любимых продуктов.
# Выведите первый, третий и последний элемент.


# TODO: решение
word = input("Введите слово: ")
print(f"Первый символ: {word[0]}")
print(f"Последний символ: {word[-1]}")
print()


# Задание 2
# Создайте список чисел [3, 7, 1, 9, 4].
# Выведите сумму, минимальное и максимальное число.


# TODO: решение
text = input("Введите строку: ")
print(f"Длина строки: {len(text)} символов")
print()

# Задание 3
# Создайте пустой список.
# Спросите у пользователя три имени и добавьте их в список.
# Выведите итоговый список.


# TODO: решение
name = input("Введите имя: ")
clean_name = name.strip().capitalize()
print(f"Обработанное имя: {clean_name}")
print()


# Задание 4
# Дан список numbers = [1, 2, 3, 4, 5, 6, 7, 8].
# Создайте новый список только из четных чисел.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# TODO: решение
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

# Задание 5
# Дан список grades = [5, 4, 3, 5, 2, 4, 5].
# Посчитайте среднюю оценку.

grades = [5, 4, 3, 5, 2, 4, 5]

# TODO: решение
grades = [5, 4, 3, 5, 2, 4, -5]
average = sum(grades) / len(grades)
print(average)

# Задание 6
# Спросите у пользователя пять чисел.
# Добавьте их в список.
# Выведите список в отсортированном виде.


# TODO: решение
numbers = []
num1 = int(input("Введите число: "))
numbers.append(num1)
num2 = int(input("Введите число: "))
numbers.append(num2)
num3 = int(input("Введите число: "))
numbers.append(num3)
num4 = int(input("Введите число: "))
numbers.append(num4)
num5 = int(input("Введите число: "))
numbers.append(num5)
print(sorted(numbers))