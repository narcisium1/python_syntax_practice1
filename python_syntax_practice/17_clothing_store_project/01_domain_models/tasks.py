"""
Этап 01. Доменные модели магазина одежды

Цель: описать основные объекты предметной области без подключения к БД,
меню, репозиториев и сервисов.

Модели создавайте прямо в этом файле. Следующие этапы будут импортировать
их отсюда, а не копировать классы заново.
"""


# Задание 1
# Опишите модель категории одежды.
# Категория должна хранить идентификатор, название и краткое описание.


# TODO: добавить модель категории
class Category:
    def __init__(self, category_id, name, description):
        if category_id <= 0:
            raise ValueError("ID категории должен быть положительным числом")
        if not name or not name.strip():
            raise ValueError("Название категории не может быть пустым")
        
        self.category_id = category_id
        self.name = name.strip()
        self.description = description.strip() if description else ""

    def __str__(self):
        return f"Категория: {self.name}"

    def __repr__(self):
        return f"Category(id={self.category_id}, name='{self.name}')"



# Задание 2
# Опишите модель товара.
# Продумайте поля для идентификатора, названия, категории, цены, цвета,
# описания и активности товара.


# TODO: добавить модель товара
class Product:
    def __init__(self, product_id, name, category, price, color, description="", is_active=True):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.color = color
        self.description = description
        self.is_active = is_active

# Задание 3
# Добавьте проверки для данных товара.
# Обратите внимание на цену, пустое название и связь с категорией.


# TODO: добавить защиту состояния товара
class Product:
    def __init__(self, product_id, name, category, price, color, description="", is_active=True):
        # Проверка ID
        if product_id <= 0:
            raise ValueError("ID товара должен быть положительным числом")
        
        # Проверка названия
        if not name or not name.strip():
            raise ValueError("Название товара не может быть пустым")
        
        # Проверка категории
        if not isinstance(category, Category):
            raise ValueError("Категория должна быть объектом Category")
        
        # Проверка цены
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        
        # Проверка цвета
        if not color or not color.strip():
            raise ValueError("Цвет товара не может быть пустым")
        
        self.product_id = product_id
        self.name = name.strip()
        self.category = category
        self.price = price
        self.color = color.strip()
        self.description = description.strip() if description else ""
        self.is_active = is_active

    def __str__(self):
        return f"Товар: {self.name}, Цена: {self.price} руб., Цвет: {self.color}"

    def __repr__(self):
        return f"Product(id={self.product_id}, name='{self.name}', price={self.price})"

# Задание 4
# Опишите модель остатка товара по размеру.
# Она должна связывать товар, размер и количество этого размера на складе.


# TODO: добавить модель остатка по размеру
class SizeStock:
    # Допустимые размеры одежды
    VALID_SIZES = ["XS", "S", "M", "L", "XL", "XXL"]
    
    def __init__(self, product, size, quantity):
        if not isinstance(product, Product):
            raise ValueError("Должен быть указан объект Product")
        
        if size not in self.VALID_SIZES:
            raise ValueError(f"Размер должен быть из {self.VALID_SIZES}")
        
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")
        
        self.product = product
        self.size = size
        self._quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    def add_stock(self, amount):
        """Добавить товар на склад"""
        if amount <= 0:
            raise ValueError("Количество для добавления должно быть положительным")
        self._quantity += amount

    def remove_stock(self, amount):
        """Удалить товар со склада (при продаже)"""
        if amount <= 0:
            raise ValueError("Количество для удаления должно быть положительным")
        if amount > self._quantity:
            raise ValueError(f"Недостаточно товара. Доступно: {self._quantity}")
        self._quantity -= amount

    def is_available(self, requested_quantity=1):
        """Проверить, доступен ли товар в нужном количестве"""
        return self._quantity >= requested_quantity and self.product.is_active

    def __str__(self):
        return f"{self.product.name} ({self.size}): {self._quantity} шт."

    def __repr__(self):
        return f"SizeStock(product='{self.product.name}', size='{self.size}', quantity={self._quantity})"

# Задание 5
# Добавьте поведение товара.
# Товар или отдельная модель остатка должны помогать понять,
# доступен ли конкретный размер и какое количество можно купить.


# TODO: добавить методы изменения и проверки товара
class Product:
    def __init__(self, product_id, name, category, price, color, description="", is_active=True):
        if product_id <= 0:
            raise ValueError("ID товара должен быть положительным числом")
        if not name or not name.strip():
            raise ValueError("Название товара не может быть пустым")
        if not isinstance(category, Category):
            raise ValueError("Категория должна быть объектом Category")
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if not color or not color.strip():
            raise ValueError("Цвет товара не может быть пустым")
        
        self.product_id = product_id
        self.name = name.strip()
        self.category = category
        self.price = price
        self.color = color.strip()
        self.description = description.strip() if description else ""
        self.is_active = is_active
        self._sizes_stock = {}  # словарь для хранения остатков по размерам

    def add_size_stock(self, size, quantity):
        """Добавить остаток по размеру"""
        if size in self._sizes_stock:
            self._sizes_stock[size].add_stock(quantity)
        else:
            self._sizes_stock[size] = SizeStock(self, size, quantity)

    def get_size_stock(self, size):
        """Получить остаток по размеру"""
        return self._sizes_stock.get(size)

    def is_size_available(self, size, quantity=1):
        """Проверить доступность размера"""
        stock = self._sizes_stock.get(size)
        if not stock:
            return False
        return stock.is_available(quantity) and self.is_active

    def get_available_sizes(self):
        """Получить список доступных размеров"""
        return [size for size, stock in self._sizes_stock.items() if stock.is_available()]

    def get_price_with_discount(self, discount_percent):
        """Вычислить цену со скидкой"""
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Скидка должна быть от 0 до 100 процентов")
        return round(self.price * (100 - discount_percent) / 100, 2)

    def deactivate(self):
        """Деактивировать товар"""
        self.is_active = False

    def activate(self):
        """Активировать товар"""
        self.is_active = True

    def __str__(self):
        status = "Активен" if self.is_active else "Неактивен"
        return f"Товар: {self.name}, Цена: {self.price} руб., Цвет: {self.color}, {status}"

    def __repr__(self):
        return f"Product(id={self.product_id}, name='{self.name}', price={self.price})"

# Задание 6
# Опишите модель покупателя.
# Продумайте поля для идентификатора, имени, телефона и email.


# TODO: добавить модель покупателя
class Customer:
    def __init__(self, customer_id, full_name, phone, email):
        if customer_id <= 0:
            raise ValueError("ID покупателя должен быть положительным числом")
        if not full_name or not full_name.strip():
            raise ValueError("Имя покупателя не может быть пустым")
        if not phone or not phone.strip():
            raise ValueError("Телефон не может быть пустым")
        if not email or "@" not in email or "." not in email:
            raise ValueError("Некорректный email адрес")
        
        self.customer_id = customer_id
        self.full_name = full_name.strip()
        self.phone = phone.strip()
        self.email = email.strip()
        self._order_history = []  # список заказов

    def add_to_order_history(self, order):
        """Добавить заказ в историю"""
        self._order_history.append(order)

    def get_order_history(self):
        """Получить историю заказов"""
        return self._order_history.copy()

    def __str__(self):
        return f"Покупатель: {self.full_name}, Телефон: {self.phone}, Email: {self.email}"

    def __repr__(self):
        return f"Customer(id={self.customer_id}, name='{self.full_name}')"

# Задание 7
# Создайте несколько объектов и проверьте, что корректные данные принимаются,
# а некорректные приводят к понятной ошибке.


# TODO: добавить ручную проверку моделей
if __name__ == "__main__":
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ДОМЕННЫХ МОДЕЛЕЙ МАГАЗИНА ОДЕЖДЫ")
    print("=" * 60)
    
    # Тестирование категории
    print("\n1. ТЕСТИРОВАНИЕ КАТЕГОРИИ")
    print("-" * 40)
    try:
        category1 = Category(1, "Футболки", "Мужские и женские футболки")
        category2 = Category(2, "Джинсы", "Классические и современные джинсы")
        print(f"✓ Создана категория: {category1}")
        print(f"✓ Создана категория: {category2}")
        
        # Проверка ошибок
        try:
            Category(0, "Тест", "Описание")
        except ValueError as e:
            print(f"✓ Ошибка при создании с ID=0: {e}")
        
        try:
            Category(3, "", "Описание")
        except ValueError as e:
            print(f"✓ Ошибка при пустом названии: {e}")
            
    except Exception as e:
        print(f"✗ Ошибка: {e}")
    
    # Тестирование товара
    print("\n2. ТЕСТИРОВАНИЕ ТОВАРА")
    print("-" * 40)
    try:
        category = Category(1, "Футболки", "Мужские и женские футболки")
        product = Product(1, "Classic T-Shirt", category, 1999, "Белый", "Хлопковая футболка")
        print(f"✓ Создан товар: {product}")
        
        # Проверка скидки
        discounted_price = product.get_price_with_discount(20)
        print(f"✓ Цена со скидкой 20%: {discounted_price} руб.")
        
        # Проверка добавления размеров
        product.add_size_stock("M", 10)
        product.add_size_stock("L", 5)
        product.add_size_stock("XL", 3)
        print(f"✓ Добавлены размеры: M, L, XL")
        
        # Проверка доступности
        print(f"✓ Размер M доступен: {product.is_size_available('M', 2)}")
        print(f"✓ Размер XXL доступен: {product.is_size_available('XXL')}")
        print(f"✓ Доступные размеры: {product.get_available_sizes()}")
        
        # Проверка ошибок
        try:
            Product(-1, "Test", category, 100, "Красный")
        except ValueError as e:
            print(f"✓ Ошибка при отрицательном ID: {e}")
        
        try:
            Product(2, "", category, 100, "Красный")
        except ValueError as e:
            print(f"✓ Ошибка при пустом названии: {e}")
        
        try:
            Product(2, "Test", category, -50, "Красный")
        except ValueError as e:
            print(f"✓ Ошибка при отрицательной цене: {e}")
            
    except Exception as e:
        print(f"✗ Ошибка: {e}")
    
    # Тестирование остатка по размеру
    print("\n3. ТЕСТИРОВАНИЕ ОСТАТКА ПО РАЗМЕРУ")
    print("-" * 40)
    try:
        category = Category(1, "Футболки", "Описание")
        product = Product(1, "T-Shirt", category, 1999, "Белый")
        
        stock = SizeStock(product, "M", 15)
        print(f"✓ Создан остаток: {stock}")
        
        stock.add_stock(5)
        print(f"✓ После добавления 5: {stock.quantity} шт.")
        
        stock.remove_stock(3)
        print(f"✓ После удаления 3: {stock.quantity} шт.")
        
        print(f"✓ Доступно 10 шт: {stock.is_available(10)}")
        print(f"✓ Доступно 20 шт: {stock.is_available(20)}")
        
        # Проверка ошибок
        try:
            SizeStock(product, "Invalid", 10)
        except ValueError as e:
            print(f"✓ Ошибка при неверном размере: {e}")
        
        try:
            stock.remove_stock(100)
        except ValueError as e:
            print(f"✓ Ошибка при удалении большего количества: {e}")
            
    except Exception as e:
        print(f"✗ Ошибка: {e}")
    
    # Тестирование покупателя
    print("\n4. ТЕСТИРОВАНИЕ ПОКУПАТЕЛЯ")
    print("-" * 40)
    try:
        customer = Customer(1, "Иванов Иван Иванович", "+7(999)123-45-67", "ivan@example.com")
        print(f"✓ Создан покупатель: {customer}")
        
        # Проверка ошибок
        try:
            Customer(1, "Иван", "123", "invalid-email")
        except ValueError as e:
            print(f"✓ Ошибка при неверном email: {e}")
        
        try:
            Customer(1, "", "123", "test@mail.ru")
        except ValueError as e:
            print(f"✓ Ошибка при пустом имени: {e}")
            
    except Exception as e:
        print(f"✗ Ошибка: {e}")
    
    # Комплексный тест
    print("\n5. КОМПЛЕКСНЫЙ ТЕСТ ВСЕХ МОДЕЛЕЙ")
    print("-" * 40)
    try:
        # Создаем категорию
        category = Category(10, "Свитера", "Теплые и стильные свитера")
        
        # Создаем товар
        sweater = Product(
            product_id=100,
            name="Шерстяной свитер",
            category=category,
            price=3500,
            color="Синий",
            description="100% шерсть, теплый и мягкий"
        )
        
        # Добавляем размеры
        sweater.add_size_stock("S", 5)
        sweater.add_size_stock("M", 8)
        sweater.add_size_stock("L", 10)
        sweater.add_size_stock("XL", 3)
        
        # Создаем покупателя
        customer = Customer(1000, "Петрова Анна Сергеевна", "+7(916)987-65-43", "anna@example.com")
        
        # Выводим информацию
        print(f"Категория: {category.name}")
        print(f"Товар: {sweater.name}")
        print(f"Цена: {sweater.price} руб.")
        print(f"Доступные размеры: {sweater.get_available_sizes()}")
        print(f"Количество М: {sweater.get_size_stock('M').quantity} шт.")
        print(f"Покупатель: {customer.full_name}")
        
        # Проверяем возможность покупки
        if sweater.is_size_available("M", 2):
            print("✓ Можно купить 2 свитера размера M")
            sweater.get_size_stock("M").remove_stock(2)
            print(f"  Остаток M после покупки: {sweater.get_size_stock('M').quantity} шт.")
        
        print("\n" + "=" * 60)
        print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
        print("=" * 60)
        
    except Exception as e:
        print(f"✗ Ошибка в комплексном тесте: {e}")