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
store3 = Store("Wildberries", "Ленина 38")

store1.add_item("apples", 100.50)
store1.add_item("bananas", 50.75)

store2.add_item("milk", 75.0)
store2.add_item("bread", 41.50)

store3.add_item("eggs", 102.0)
store3.add_item("butter", 153.0)

# Тестирование методов
print(store1)
store1.update_price("apples", 50.60)
print(f"Цена яблок: {store1.get_price('apples')}")
store1.remove_item("bananas")
print(store1)