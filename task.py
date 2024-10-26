class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    def __str__(self):
        return f"Магазин: {self.name}, Адрес: {self.address}, Товары: {self.items}"

# Создание объектов класса Store
store1 = Store("Магнит", "Иванова 1")
store2 = Store("Пятерочка", "Октябрьская 10")
store3 = Store("Дикси", "Ленина 38")

store1.add_item("яблоки", 100.50)
store1.add_item("бананы", 50.75)

store2.add_item("молоко", 75.0)
store2.add_item("хлеб", 41.50)

store3.add_item("яйца", 102.0)
store3.add_item("сливочное масло", 153.0)

# Тестирование методов для store2
print("Тестирование методов для Пятерочки:")
print(store2)

# Добавление товара
store2.add_item("сахар", 45.0)
print("Добавлен сахар:")
print(store2)

# Обновление цены товара
store2.update_price("молоко", 80.0)
print("Цена молока обновлена:")
print(store2)

# Запрос цены товара
price = store2.get_price("хлеб")
print(f"Цена хлеба: {price}")

# Удаление товара
store2.remove_item("хлеб")
print("Хлеб удален:")
print(store2)