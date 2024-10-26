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