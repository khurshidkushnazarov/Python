# Homework 1. ToDo List Application

# 1 Define Task Class:
# Create a Task class with attributes such as task title, description, due date, and status.

class Task:
    def __init__(self, title, description, due_date, status):
        self.title = title            # вазифа номи
        self.description = description  # тавсифи
        self.due_date = due_date      # тугаш санаси
        self.status = status          # ҳолати

    def __str__(self):
        return (f"Вазифа: {self.title}\n"
                f"Тавсифи: {self.description}\n"
                f"Тугаш санаси: {self.due_date}\n"
                f"Ҳолати: {self.status}")
    
task1 = Task("Ҳужжат тайёрлаш", "Лойиҳа учун ҳужжат тайёрлаш", "2025-09-10", "Бажарилмоқда")

print(task1)


# 2 Define ToDoList Class:
# Create a ToDoList class that manages a list of tasks.
# Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.


class Task:
    def __init__(self, title, description, due_date, status="Бажарилмоқда"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_done(self):
        self.status = "Бажарилган"

    def __str__(self):
        return (f"Вазифа: {self.title}\n"
                f"Тавсифи: {self.description}\n"
                f"Тугаш санаси: {self.due_date}\n"
                f"Ҳолати: {self.status}")

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Вазифа '{task.title}' қўшилди.")

    def mark_task_done(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_done()
                print(f"Вазифа '{title}' бажарилган деб белгиланди.")
                return
        print(f"Вазифа '{title}' топилмади.")

    def show_all_tasks(self):
        if not self.tasks:
            print("Вазифалар рўйхати бўш.")
            return
        print("Барча вазифалар:")
        for task in self.tasks:
            print("--------------------")
            print(task)

    def show_pending_tasks(self):
        pending = [task for task in self.tasks if task.status != "Бажарилган"]
        if not pending:
            print("Барча вазифалар бажарилган.")
            return
        print("Бажарилмаган вазифалар:")
        for task in pending:
            print("--------------------")
            print(task)


# 3 Create Main Program:
# Develop a simple CLI to interact with the ToDoList.
# Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.

class Task:
    def __init__(self, title, description, due_date, status="Бажарилмоқда"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_done(self):
        self.status = "Бажарилган"

    def __str__(self):
        return (f"Вазифа: {self.title}\n"
                f"Тавсифи: {self.description}\n"
                f"Тугаш санаси: {self.due_date}\n"
                f"Ҳолати: {self.status}")

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Вазифа '{task.title}' қўшилди.")

    def mark_task_done(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_done()
                print(f"Вазифа '{title}' бажарилган деб белгиланди.")
                return
        print(f"Вазифа '{title}' топилмади.")

    def show_all_tasks(self):
        if not self.tasks:
            print("Вазифалар рўйхати бўш.")
            return
        print("Барча вазифалар:")
        for task in self.tasks:
            print("--------------------")
            print(task)

    def show_pending_tasks(self):
        pending = [task for task in self.tasks if task.status != "Бажарилган"]
        if not pending:
            print("Барча вазифалар бажарилган.")
            return
        print("Бажарилмаган вазифалар:")
        for task in pending:
            print("--------------------")
            print(task)


def main():
    todo = ToDoList()

    while True:
        print("\n--- ToDoList Менюси ---")
        print("1. Янги вазифа қўшиш")
        print("2. Вазифани бажарилган деб белгилаш")
        print("3. Барча вазифаларни кўрсатиш")
        print("4. Фақат бажарилмаган вазифаларни кўрсатиш")
        print("5. Чиқиш")

        choice = input("Танловингизни киритинг (1-5): ")

        if choice == "1":
            title = input("Вазифа номини киритинг: ")
            description = input("Вазифа тавсифини киритинг: ")
            due_date = input("Тугаш санасини киритинг (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            todo.add_task(task)

        elif choice == "2":
            title = input("Бажарилган деб белгиланадиган вазифа номини киритинг: ")
            todo.mark_task_done(title)

        elif choice == "3":
            todo.show_all_tasks()

        elif choice == "4":
            todo.show_pending_tasks()

        elif choice == "5":
            print("Дастур якунланмоқда. Хайр!")
            break

        else:
            print("Нотоғри танлов. Илтимос, 1-5 орасида рақам киритинг.")

if __name__ == "__main__":
    main()


# 4 Test the Application:
# Create instances of tasks and test the functionality of your ToDoList.

todo = ToDoList()

task1 = Task("Ҳужжат тайёрлаш", "Лойиҳа ҳужжати тайёрлаш", "2025-09-10")
task2 = Task("Учрашувга тайёрланиш", "Келаси ҳафтаги учрашувга тайёрланиш", "2025-09-05")
task3 = Task("Тахрир қилиш", "Мақолани такрорий кўриб чиқиш", "2025-09-08")

todo.add_task(task1)
todo.add_task(task2)
todo.add_task(task3)

print("\nБарча вазифалар:")
todo.show_all_tasks()

todo.mark_task_done("Учрашувга тайёрланиш")

print("\nБажарилмаган вазифалар:")
todo.show_pending_tasks()
