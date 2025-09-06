# 1.Create your own virtual environment and install some python packages.
# 2.Create custom modules.
# Create math_operations.py module. Define add, subtract, multiply and divide functions in it. (All functions accept two arguments in this task)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("0 га бўлиш мумкин эмас")
    return a / b


# Create string_utils.py module. Define reverse_string and count_vowels functions in it. (All functions accept one argument in this task)

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count


# 3.Create custom packages.
# Create geometry package.
# import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius

# Create file_operations package.

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


