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
