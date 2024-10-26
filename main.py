class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_incomplete_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def show_tasks(self):
        for task in self.tasks:
            print(task)

task_manager = TaskManager()
task1 = Task("Купить продукты", "2024-06-12")
task2 = Task("Сделать домашнее задание", "2024-06-15")

task_manager.add_task(task1)
task_manager.add_task(task2)

task2.mark_completed()

task_manager.show_tasks()

task1.mark_completed()

print("\nТекущие задачи:")
incomplete_tasks = task_manager.get_incomplete_tasks()
for task in incomplete_tasks:
    print(task)

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