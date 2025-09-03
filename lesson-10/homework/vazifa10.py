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


# Homework 2. Simple Blog System

# 1.Define Post Class:
# Create a Post class with attributes like title, content, and author.

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return (f"Пост номи: {self.title}\n"
                f"Мазмуни: {self.content}\n"
                f"Муаллиф: {self.author}")
    
post1 = Post("Янги мақола", "Бу мақолада Python ҳақида маълумот берилади.", "Аҳмаджон")

print(post1)


# 2. Define Blog Class:
# Create a Blog class that manages a list of posts.
# Include methods to add a post, list all posts, and display posts by a specific author.

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return (f"Пост номи: {self.title}\n"
                f"Мазмуни: {self.content}\n"
                f"Муаллиф: {self.author}")

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"Пост '{post.title}' қўшилди.")

    def show_all_posts(self):
        if not self.posts:
            print("Блогда ҳали постлар йўқ.")
            return
        print("Барча постлар:")
        for post in self.posts:
            print("------------------------")
            print(post)

    def show_posts_by_author(self, author):
        filtered = [post for post in self.posts if post.author == author]
        if not filtered:
            print(f"Муаллиф '{author}'нинг постлари топилмади.")
            return
        print(f"Муаллиф '{author}'нинг постлари:")
        for post in filtered:
            print("------------------------")
            print(post)

blog = Blog()

post1 = Post("Python асослари", "Бу постда Python асослари ёритилган.", "Аҳмад")
post2 = Post("AI ва келажак", "AI технологиялари ҳақида фикрлар.", "Зуҳра")
post3 = Post("Python мисоллари", "Фойдали Python кодлари.", "Аҳмад")

blog.add_post(post1)
blog.add_post(post2)
blog.add_post(post3)

print("\nБарча постлар:")
blog.show_all_posts()

print("\nФақат 'Аҳмад' муаллифининг постлари:")
blog.show_posts_by_author("Аҳмад")


# 3. Create Main Program:
# Develop a CLI to interact with the Blog system.
# Include options to add posts, list all posts, and display posts by a specific author.


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return (f"Пост номи: {self.title}\n"
                f"Мазмуни: {self.content}\n"
                f"Муаллиф: {self.author}")


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"\n Пост '{post.title}' муваффақиятли қўшилди.")

    def show_all_posts(self):
        if not self.posts:
            print("\n Блогда ҳали постлар йўқ.")
            return
        print("\nБарча постлар:")
        for post in self.posts:
            print("------------------------")
            print(post)

    def show_posts_by_author(self, author):
        filtered = [post for post in self.posts if post.author == author]
        if not filtered:
            print(f"\nМуаллиф '{author}'нинг постлари топилмади.")
            return
        print(f"\n Муаллиф '{author}'нинг постлари:")
        for post in filtered:
            print("------------------------")
            print(post)


def main():
    blog = Blog()

    while True:
        print("\n===  Blog Менюси ===")
        print("1. Янги пост қўшиш")
        print("2. Барча постларни кўриш")
        print("3. Муаллиф бўйича постларни кўриш")
        print("4. Чиқиш")

        choice = input("Танловингизни киритинг (1-4): ")

        if choice == "1":
            title = input("Пост номини киритинг: ")
            content = input("Пост мазмунини киритинг: ")
            author = input("Муаллиф номини киритинг: ")
            post = Post(title, content, author)
            blog.add_post(post)

        elif choice == "2":
            blog.show_all_posts()

        elif choice == "3":
            author = input("Муаллиф номини киритинг: ")
            blog.show_posts_by_author(author)

        elif choice == "4":
            print(" Дастур якунланди. Хайр!")
            break

        else:
            print(" Нотўғри танлов. Илтимос, 1-4 орасида рақам киритинг.")


if __name__ == "__main__":
    main()


# 4.Enhance Blog System:
# Add functionality to delete a post, edit a post, and display the latest posts.

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Пост: {self.title}\nМуаллиф: {self.author}\nМазмун: {self.content}"
    
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def show_all_posts(self):
        if not self.posts:
            print("Постлар йўқ.")
        else:
            for post in self.posts:
                print("---------------")
                print(post)

    def delete_post(self, title):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                print(f"'{title}' ўчирилди.")
                return
        print("Пост топилмади.")

    def edit_post(self, title):
        for post in self.posts:
            if post.title == title:
                new_title = input("Янги ном: ")
                new_content = input("Янги мазмун: ")
                new_author = input("Янги муаллиф: ")
                post.title = new_title
                post.content = new_content
                post.author = new_author
                print("Пост таҳрирланди.")
                return
        print("Пост топилмади.")

    def show_latest_posts(self, count):
        latest = self.posts[-count:]
        for post in reversed(latest):  
            print("---------------")
            print(post)


def main():
    blog = Blog()

    while True:
        print("\n--- Blog Меню ---")
        print("1. Пост қўшиш")
        print("2. Барча постларни кўриш")
        print("3. Постни ўчириш")
        print("4. Постни таҳрир қилиш")
        print("5. Сўнгги постларни кўриш")
        print("6. Чиқиш")

        tanlov = input("Танловингизни киритинг: ")

        if tanlov == "1":
            title = input("Пост номи: ")
            content = input("Мазмун: ")
            author = input("Муаллиф: ")
            post = Post(title, content, author)
            blog.add_post(post)

        elif tanlov == "2":
            blog.show_all_posts()

        elif tanlov == "3":
            title = input("Ўчириш учун пост номи: ")
            blog.delete_post(title)

        elif tanlov == "4":
            title = input("Таҳрир қилиш учун пост номи: ")
            blog.edit_post(title)

        elif tanlov == "5":
            try:
                count = int(input("Нечта сўнгги постни кўришни хоҳлайсиз? "))
            except ValueError:
                count = 3
            blog.show_latest_posts(count)

        elif tanlov == "6":
            print("Дастур якунланди.")
            break

        else:
            print("Нотўғри танлов. Қайта урининг.")


# 5. Test the Application:
# Create instances of posts and test the functionality of your Blog system.

def test_blog():
    blog = Blog()

    post1 = Post("Python", "Python дастурлаш тили ҳақида", "Аҳмад")
    post2 = Post("AI", "Сунъий интеллект ҳақида маълумот", "Зуҳра")
    post3 = Post("Web", "Веб дастурлаш асослари", "Али")
    post4 = Post("Django", "Django framework", "Аҳмад")

    
    blog.add_post(post1)
    blog.add_post(post2)
    blog.add_post(post3)
    blog.add_post(post4)

    
    print("\n--- Барча постлар ---")
    blog.show_all_posts()

    
    print("\n--- 'AI' постини таҳрирлаш ---")
    blog.edit_post("AI")  

   
    print("\n--- 'Web' постини ўчириш ---")
    blog.delete_post("Web")

   
    print("\n--- Янгиланган постлар ---")
    blog.show_all_posts()

    
    print("\n--- Сўнгги 2 пост ---")
    blog.show_latest_posts(2)


test_blog()

# Homework 3. Simple Banking System
# 1. Define Account Class:
# Create an Account class with attributes like account number, account holder name, and balance.

class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number       
        self.holder_name = holder_name                
        self.balance = balance                        

    def __str__(self):
        return (f"Ҳисоб рақами: {self.account_number}\n"
                f"Ҳисоб эгаси: {self.holder_name}\n"
                f"Қолдиқ: {self.balance}")


# 2.Define Bank Class:
# Create a Bank class that manages a list of accounts.
# Include methods to add an account, check balance, deposit money, and withdraw money.

class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def __str__(self):
        return (f"Ҳисоб рақами: {self.account_number}\n"
                f"Ҳисоб эгаси: {self.holder_name}\n"
                f"Қолдиқ: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}  # account_number: Account объект

    def add_account(self, account):
        if account.account_number in self.accounts:
            print("Бундай ҳисоб рақами аллақачон мавжуд!")
        else:
            self.accounts[account.account_number] = account
            print(f"Янги ҳисоб рақами {account.account_number} қўшилди.")

    def check_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Қолдиқ: {account.balance}")
            return account.balance
        else:
            print("Ҳисоб рақами топилмади.")
            return None

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if amount > 0:
                account.balance += amount
                print(f"{amount} сўм ҳисоб рақамига қўйилди. Ягона қолдиқ: {account.balance}")
            else:
                print("Миқдор мусбат бўлиши керак.")
        else:
            print("Ҳисоб рақами топилмади.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if 0 < amount <= account.balance:
                account.balance -= amount
                print(f"{amount} сўм чиқарилди. Ягона қолдиқ: {account.balance}")
            else:
                print("Нотўғри ёки етарли маблағ йўқ.")
        else:
            print("Ҳисоб рақами топилмади.")

            
bank = Bank()

acc1 = Account("12345", "Аҳмад", 1000)
acc2 = Account("67890", "Зуҳра")

bank.add_account(acc1)
bank.add_account(acc2)

bank.check_balance("12345")
bank.deposit("67890", 500)
bank.withdraw("12345", 300)
bank.check_balance("12345")
bank.check_balance("67890")



# 3.Create Main Program:
# Develop a CLI to interact with the Banking system.
# Include options to add accounts, check balance, deposit money, and withdraw money.

class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        if account.account_number in self.accounts:
            print("Бундай ҳисоб рақами аллақачон мавжуд!")
        else:
            self.accounts[account.account_number] = account
            print(f"Янги ҳисоб рақами {account.account_number} қўшилди.")

    def check_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Қолдиқ: {account.balance}")
            return account.balance
        else:
            print("Ҳисоб рақами топилмади.")
            return None

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if amount > 0:
                account.balance += amount
                print(f"{amount} сўм ҳисоб рақамига қўйилди. Қолдиқ: {account.balance}")
            else:
                print("Миқдор мусбат бўлиши керак.")
        else:
            print("Ҳисоб рақами топилмади.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if 0 < amount <= account.balance:
                account.balance -= amount
                print(f"{amount} сўм чиқарилди. Қолдиқ: {account.balance}")
            else:
                print("Нотўғри ёки етарли маблағ йўқ.")
        else:
            print("Ҳисоб рақами топилмади.")

def main():
    bank = Bank()

    while True:
        print("\n--- Банк тизими ---")
        print("1. Ҳисоб очиш")
        print("2. Қолдиқни текшириш")
        print("3. Пул қўйиш")
        print("4. Пул ечиш")
        print("5. Чиқиш")

        choice = input("Танловингизни киритинг: ")

        if choice == "1":
            acc_num = input("Ҳисоб рақамини киритинг: ")
            name = input("Ҳисоб эгасининг исмини киритинг: ")
            try:
                balance = float(input("Бошланғич қолдиқ (агар йўқ бўлса 0): "))
            except ValueError:
                balance = 0
            account = Account(acc_num, name, balance)
            bank.add_account(account)

        elif choice == "2":
            acc_num = input("Ҳисоб рақамини киритинг: ")
            bank.check_balance(acc_num)

        elif choice == "3":
            acc_num = input("Ҳисоб рақамини киритинг: ")
            try:
                amount = float(input("Қанча пул қўймоқчисиз: "))
            except ValueError:
                print("Нотўғри миқдор!")
                continue
            bank.deposit(acc_num, amount)

        elif choice == "4":
            acc_num = input("Ҳисоб рақамини киритинг: ")
            try:
                amount = float(input("Қанча пул ечмоқчисиз: "))
            except ValueError:
                print("Нотўғри миқдор!")
                continue
            bank.withdraw(acc_num, amount)

        elif choice == "5":
            print("Дастурдан чиқилди.")
            break

        else:
            print("Нотўғри танлов. Қайта уриниб кўринг.")

if __name__ == "__main__":
    main()


# 4. Enhance Banking System:
# Add functionality to transfer money between accounts, display account details, and handle account overdrafts.

class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def __str__(self):
        return (f"Ҳисоб рақами: {self.account_number}\n"
                f"Эгаси: {self.holder_name}\n"
                f"Қолдиқ: {self.balance} сўм")

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        if account.account_number in self.accounts:
            print(" Бундай ҳисоб рақами аллақачон мавжуд!")
        else:
            self.accounts[account.account_number] = account
            print(f" Янги ҳисоб очилди: {account.account_number}")

    def check_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f" Қолдиқ: {account.balance} сўм")
            return account.balance
        else:
            print(" Ҳисоб рақами топилмади.")
            return None

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if amount > 0:
                account.balance += amount
                print(f" {amount} сўм қўшилди. Янгилангaн қолдиқ: {account.balance}")
            else:
                print(" Миқдор мусбат бўлиши керак.")
        else:
            print(" Ҳисоб рақами топилмади.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if amount <= 0:
                print(" Миқдор мусбат бўлиши керак.")
            elif amount <= account.balance:
                account.balance -= amount
                print(f" {amount} сўм ечилди. Янги қолдиқ: {account.balance}")
            else:
                print(" Етарли маблағ йўқ. Ҳаракат бекор қилинди.")
        else:
            print(" Ҳисоб рақами топилмади.")

    def transfer(self, from_acc, to_acc, amount):
        from_account = self.accounts.get(from_acc)
        to_account = self.accounts.get(to_acc)

        if not from_account or not to_account:
            print(" Ҳисоблардан бири топилмади.")
            return

        if amount <= 0:
            print(" Миқдор мусбат бўлиши керак.")
            return

        if from_account.balance < amount:
            print(" Етарли маблағ йўқ. Ўтказма бекор қилинди.")
            return

        from_account.balance -= amount
        to_account.balance += amount
        print(f" {amount} сўм {from_acc} -> {to_acc} ўтказилди.")

    def show_account_info(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(" Ҳисоб маълумотлари:")
            print(account)
        else:
            print(" Ҳисоб рақами топилмади.")


def main():
    bank = Bank()

    while True:
        print("\n=== Банк Менюси ===")
        print("1. Ҳисоб очиш")
        print("2. Қолдиқни текшириш")
        print("3. Пул қўйиш")
        print("4. Пул ечиш")
        print("5. Ҳисоблар орасида пул ўтказиш")
        print("6. Ҳисоб маълумотларини кўрсатиш")
        print("7. Чиқиш")

        choice = input("Танловингизни киритинг (1-7): ")

        if choice == "1":
            acc_num = input("Ҳисоб рақами: ")
            name = input("Ҳисоб эгаси: ")
            try:
                balance = float(input("Бошланғич қолдиқ (ихтиёрий): ") or "0")
            except ValueError:
                balance = 0
            account = Account(acc_num, name, balance)
            bank.add_account(account)

        elif choice == "2":
            acc_num = input("Ҳисоб рақами: ")
            bank.check_balance(acc_num)

        elif choice == "3":
            acc_num = input("Ҳисоб рақами: ")
            try:
                amount = float(input("Қўйиладиган сумма: "))
                bank.deposit(acc_num, amount)
            except ValueError:
                print(" Нотўғри сумма!")

        elif choice == "4":
            acc_num = input("Ҳисоб рақами: ")
            try:
                amount = float(input("Ечиладиган сумма: "))
                bank.withdraw(acc_num, amount)
            except ValueError:
                print(" Нотўғри сумма!")

        elif choice == "5":
            from_acc = input("Жўнатувчи ҳисоб рақами: ")
            to_acc = input("Қабул қилувчи ҳисоб рақами: ")
            try:
                amount = float(input("Ўтказиладиган сумма: "))
                bank.transfer(from_acc, to_acc, amount)
            except ValueError:
                print(" Нотўғри сумма!")

        elif choice == "6":
            acc_num = input("Ҳисоб рақами: ")
            bank.show_account_info(acc_num)

        elif choice == "7":
            print(" Дастур якунланди. Хайр!")
            break

        else:
            print(" Нотўғри танлов. Қайта урининг.")



# 5.Test the Application:
# Create instances of accounts and test the functionality of your Banking system.

def test_bank_system():
    bank = Bank()

    print("\n 1. Иккита ҳисоб очилмоқда...")
    acc1 = Account("1001", "Аҳмад", 1000)
    acc2 = Account("1002", "Зуҳра")
    bank.add_account(acc1)
    bank.add_account(acc2)

    print("\n 2. Қолдиқни текшириш...")
    bank.check_balance("1001")
    bank.check_balance("1002")

    print("\n 3. Пул қўйиш...")
    bank.deposit("1002", 500)
    bank.deposit("1001", 150)

    print("\n 4. Пул ечиш...")
    bank.withdraw("1001", 200)   # Етарли
    bank.withdraw("1002", 1000)  # Етарли эмас

    print("\n 5. Пул ўтказиш...")
    bank.transfer("1001", "1002", 300)  # Муваффақиятли
    bank.transfer("1002", "1001", 1000) # Етарли маблағ йўқ

    print("\n 6. Ҳисоб маълумотларини кўрсатиш...")
    bank.show_account_info("1001")
    bank.show_account_info("1002")

    print("\n 7. Нотўғри ҳисоблар билан хатоларни текшириш...")
    bank.check_balance("9999")         # Номавжуд ҳисоб
    bank.deposit("abcd", 100)          # Номавжуд ҳисоб
    bank.withdraw("abcd", 100)         # Номавжуд ҳисоб
    bank.transfer("abcd", "1001", 50)  # Нотўғри жўнатувчи
    bank.transfer("1001", "xyz", 50)   # Нотўғри қабул қилувчи

if __name__ == "__main__":
    test_bank_system()
