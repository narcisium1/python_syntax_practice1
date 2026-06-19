"""
Тема 14. Магические методы
"""


# Задание 1
# Создайте класс City с атрибутами name и population.
# Добавьте метод __str__(), который возвращает:
# Город <name>, население: <population>
# Создайте город и выведите его через print().


# TODO: решение
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        return f"Город {self.name}, население: {self.population}"

city = City("Москва", 12500000)
print(city)

# Задание 2
# Создайте класс Movie с атрибутами title и year.
# Добавьте метод __repr__(), который возвращает строку:
# Movie(title='<title>', year=<year>)
# Проверьте вывод объекта.


# TODO: решение
class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __repr__(self):
        return f"Movie(title='{self.title}', year={self.year})"

movie = Movie("Inception", 2010)
print(movie)

# Задание 3
# Создайте класс Point с атрибутами x и y.
# Добавьте метод __eq__(), чтобы две точки считались равными,
# если у них одинаковые x и y.
# Проверьте сравнение двух объектов через ==.


# TODO: решение
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

p1 = Point(3, 5)
p2 = Point(3, 5)
p3 = Point(1, 2)

print(p1 == p2) 
print(p1 == p3)  

# Задание 4
# Создайте класс Playlist.
# Внутри храните список songs.
# Добавьте метод add_song(song).
# Добавьте метод __len__(), чтобы len(playlist) возвращал количество песен.


# TODO: решение
class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

playlist = Playlist()
playlist.add_song("Bohemian Rhapsody")
playlist.add_song("Imagine")
print(len(playlist))  

# Задание 5
# Создайте класс Package с атрибутами code и weight.
# Добавьте метод __lt__(), чтобы посылки сравнивались по весу.
# Проверьте выражение package1 < package2.


# TODO: решение
class Package:
    def __init__(self, code, weight):
        self.code = code
        self.weight = weight

    def __lt__(self, other):
        if not isinstance(other, Package):
            return NotImplemented
        return self.weight < other.weight

p1 = Package("A123", 5)
p2 = Package("B456", 10)

print(p1 < p2)  

# Задание 6
# Создайте класс Wallet с атрибутами owner и amount.
# Добавьте __str__(), который возвращает:
# Кошелек <owner>: <amount> руб.
# Добавьте __eq__(), который сравнивает кошельки по owner и amount.


# TODO: решение
class Wallet:
    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount

    def __str__(self):
        return f"Кошелек {self.owner}: {self.amount} руб."

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            return False
        return self.owner == other.owner and self.amount == other.amount

w1 = Wallet("Анна", 1000)
w2 = Wallet("Анна", 1000)
w3 = Wallet("Иван", 500)

print(w1)
print(w1 == w2) 
print(w1 == w3) 