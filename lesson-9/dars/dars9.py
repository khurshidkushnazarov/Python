## CLASS, OOP


class my_class:
    pass

my_object =  my_class()
print(type(my_object))


class student:
    pass
student1 = student()
student1.age = 25
student1.name = 'Azamat'
student1.email = 'azamat1015@gmail.com'
print(student1.email)


class student:
    pass
student1 = student()
student1.age = 25
student1.name = 'Azamat'
student1.email = 'azamat1015@gmail.com'
student2 = student()
student2.age = 26
student2.name = 'Husan'
student2.email = 'husan1015@gmail.com'
print(student1.email)
print(student2.email)


class student:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
s1 = student('Azamat', 24, 'azamat1015@gmail.com')
s2 = student('Husan', 26, 'husan1015@gmail.com')
print(s1.email)
print(s2.email)


class student:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
s1 = student('Azamat', 24, 'azamat1015@gmail.com')
s2 = student('Husan', 26, 'husan1015@gmail.com')
print(s1.email,s1.age,s1.name)
print(s2.email,s2.age,s2.name)


class Employee:
    salary = 1000
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

employee1 = Employee('Azamat', 41, 2000)
print(employee1.salary)


class Employee:
    salary = 1000
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

employee1 = Employee('Azamat', 41, 2000)
print(Employee.salary)



class Employee:
    salary = 1000
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

employee1 = Employee('Azamat', 41, 2000)
employee2 = Employee('Alex', 42, 5000)
print(employee2.salary)
print(Employee.salary)


class Employee:
    bonus = 100       # 100 dollar bonus berilganda
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary+self.bonus

employee1 = Employee('Azamat', 41, 2000)
employee2 = Employee('Alex', 42, 5000)
print(employee2.salary)
print(Employee.bonus)


class Employee:
    bonus = 100  # 100 dollar bonus berilganda
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary+self.bonus

employee1 = Employee('Azamat', 41, 2000)
employee2 = Employee('Alex', 42, 5000)
print(employee2.salary)
print(employee1.salary)



class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point({self.x} {self.y})"

p1 = Point(4,3)

print(p1)



class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point({self.x} {self.y})"
    def reverse(self):
        self.x = -1 * self.x
        self.y = -1 * self.y

p1 = Point(4,3)
p1.reverse()

print(p1)


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point({self.x} {self.y})"
    def reverse(self):
        self.x = -1 * self.x
        self.y = -1 * self.y
    def reset(self):
        self.x = 0
        self.y = 0

p1 = Point(4,3)
p1.reverse()
p1.reset()

print(p1)




class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point({self.x} {self.y})"
    def reverse(self):
        self.x = -1 * self.x
        self.y = -1 * self.y
    def reset(self):
        self.x = 0
        self.y = 0
    def uzuntop(self):
        masofa = (self.x**2 + self.y**2)**0.5
        return masofa

p1 = Point(4,3)
#p1.reverse()
#p1.reset()
p1.uzuntop()

# print(p1)











