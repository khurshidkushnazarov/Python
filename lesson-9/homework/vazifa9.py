# 1. Circle Class
# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

import math

class Aylana:
    def __init__(self, radius):
        self.radius = radius

    def yuzi(self):
        return math.pi * (self.radius ** 2)

    def perimetr(self):
        return 2 * math.pi * self.radius

aylana = Aylana(5)
print("Айлананинг юзи:", aylana.yuzi())
print("Айлананинг периметри:", aylana.perimetr())

## 2. Person Class
## Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.

from datetime import datetime

class Person:
    def __init__(self, ism, mamlakat, tugilgan_sana):
        self.ism = ism
        self.mamlakat = mamlakat
              self.tugilgan_sana = datetime.strptime(tugilgan_sana, "%Y-%m-%d")

  def yosh(self):
        bugun = datetime.today()
        yosh = bugun.year - self.tugilgan_sana.year
        
        if (bugun.month, bugun.day) < (self.tugilgan_sana.month, self.tugilgan_sana.day):
            yosh -= 1
        return yosh

person = Person("Ali", "O'zbekiston", "1990-05-15")
print(f"{person.ism}ning ёши: {person.yosh()} ёшда.")


# 3. Calculator Class
# Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def qoshib_ber(self, a, b):
        return a + b

    def ayirib_ber(self, a, b):
        return a - b

    def kopaytirib_ber(self, a, b):
        return a * b

    def bolib_ber(self, a, b):
        if b == 0:
            return "Xato: 0 ga bo'lib bo'lmaydi!"
        return a / b

calc = Calculator()
print("Қўшиш:", calc.qoshib_ber(10, 5))
print("Айириш:", calc.ayirib_ber(10, 5))
print("Кўпайтириш:", calc.kopaytirib_ber(10, 5))
print("Бўлиш:", calc.bolib_ber(10, 5))
print("Бўлиш (0 га):", calc.bolib_ber(10, 0))



# 4. Shape and Subclasses
# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.

import math

class Shakl:
    def yuza(self):
        raise NotImplementedError("Bu metod subclasslarda amalga oshirilishi kerak.")

    def perimetr(self):
        raise NotImplementedError("Bu metod subclasslarda amalga oshirilishi kerak.")


class Aylana(Shakl):
    def __init__(self, radius):
        self.radius = radius

    def yuza(self):
        return math.pi * (self.radius ** 2)

    def perimetr(self):
        return 2 * math.pi * self.radius


class Uchburchak(Shakl):
    def __init__(self, tomon1, tomon2, tomon3):
        self.tomon1 = tomon1
        self.tomon2 = tomon2
        self.tomon3 = tomon3

    def perimetr(self):
        return self.tomon1 + self.tomon2 + self.tomon3

    def yuza(self):
        p = self.perimetr() / 2
        return math.sqrt(p * (p - self.tomon1) * (p - self.tomon2) * (p - self.tomon3))


class Kvadrat(Shakl):
    def __init__(self, tomon):
        self.tomon = tomon

    def yuza(self):
        return self.tomon ** 2

    def perimetr(self):
        return 4 * self.tomon


shakl1 = Aylana(5)
print("Aylana yuzi:", shakl1.yuza())
print("Aylana perimetri:", shakl1.perimetr())

shakl2 = Uchburchak(3, 4, 5)
print("Uchburchak yuzi:", shakl2.yuza())
print("Uchburchak perimetri:", shakl2.perimetr())

shakl3 = Kvadrat(4)
print("Kvadrat yuzi:", shakl3.yuza())
print("Kvadrat perimetri:", shakl3.perimetr())



# 5. Binary Search Tree Class
# Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _add_recursive(self, current_node, value):
        if current_node is None:
            return Node(value)

        if value < current_node.value:
            current_node.left = self._add_recursive(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._add_recursive(current_node.right, value)
        else:
          pass
        return current_node

    def add(self, value):
        self.root = self._add_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

bst = BinarySearchTree()
bst.add(10)
bst.add(5)
bst.add(15)
bst.add(7)

print(bst.search(7))   # True
print(bst.search(3))   # False


# 6. Stack Data Structure
# Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"{item} стекка қўшилди.")

    def pop(self):
        if self.is_empty():
            print("Стек бўш. Олиб ташлаш мумкин эмас.")
            return None
        removed_item = self.items.pop()
        print(f"{removed_item} стекдан олиб ташланди.")
        return removed_item

    def peek(self):
        if self.is_empty():
            print("Стек бўш.")
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def show(self):
        print("Жорий стек:", self.items)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.show()

stack.pop()
stack.show()


# 7. Linked List Data Structure
# Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        if not current:
            print("Рўйхат бўш.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
        print(f"{data} топилмади.")



# 8. Shopping Cart Class
# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, nomi, narxi):
        self.items.append({"nomi": nomi, "narxi": narxi})
        print(f"{nomi} ({narxi} сўм) саватчага қўшилди.")

    def remove_item(self, nomi):
        for item in self.items:
            if item["nomi"] == nomi:
                self.items.remove(item)
                print(f"{nomi} саватчадан ўчирилди.")
                return
        print(f"{nomi} саватчада топилмади.")

    def get_total(self):
        total = sum(item["narxi"] for item in self.items)
        return total

    def show_cart(self):
        if not self.items:
            print("Саватча бўш.")
        else:
            print("Саватчадаги маҳсулотлар:")
            for item in self.items:
                print(f"- {item['nomi']} : {item['narxi']} сўм")
            print(f"Жами нарх: {self.get_total()} сўм")



# 9. Stack with Display
# Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, element):
        self.items.append(element)
        print(f"{element} стекка қўшилди.")

    def pop(self):
        if self.is_empty():
            print("Стек бўш, олиб ташлаб бўлмайди.")
            return None
        removed = self.items.pop()
        print(f"{removed} стекдан олиб ташланди.")
        return removed

    def display(self):
        if self.is_empty():
            print("Стек бўш.")
        else:
            print("Стекдаги элементлар (охиридан бошлаб):")
            for item in reversed(self.items):
                print(item)


# 10. Queue Data Structure
# Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, element):
        self.items.append(element)
        print(f"{element} навбатга қўшилди.")

    def dequeue(self):
        if not self.items:
            print("Навбат бўш. Олиб ташлаб бўлмайди.")
            return None
        removed = self.items.pop(0)
        print(f"{removed} навбатдан олиб ташланди.")
        return removed

    def display(self):
        if not self.items:
            print("Навбат бўш.")
        else:
            print("Навбатдаги элементлар:")
            for item in self.items:
                print(item)


# 11. Bank Class
# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.


class Bank:
    def __init__(self):
        self.accounts = {}  # {ism: balans}

    def add_client(self, name):
        if name not in self.accounts:
            self.accounts[name] = 0
            print(f"{name} мижоз қўшилди.")
        else:
            print(f"{name} аллақачон мавжуд.")

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount
            print(f"{name} ҳисобига {amount} сўм қўшилди.")
        else:
            print(f"{name} мижоз топилмади.")

    def withdraw(self, name, amount):
        if name in self.accounts:
            if self.accounts[name] >= amount:
                self.accounts[name] -= amount
                print(f"{name} ҳисобидан {amount} сўм ечилди.")
            else:
                print(f"{name} ҳисобида етарли маблағ йўқ.")
        else:
            print(f"{name} мижоз топилмади.")

    def show_balance(self, name):
        if name in self.accounts:
            print(f"{name} ҳисоби: {self.accounts[name]} сўм")
        else:
            print(f"{name} мижоз топилмади.")


