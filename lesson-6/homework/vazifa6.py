## 1. Modify String with Underscores

def pastki_chiziq_qoshish(txt):
    natija = []
    unli = "aeiou"
    i = 0
    while i < len(txt):
        natija.append(txt[i])
        if (i + 1) % 3 == 0 and i < len(txt) - 1:
            if txt[i] in unli or txt[i + 1] == '_':
                natija.append(txt[i + 1])
                natija.append('_')
                i += 1
            else:
                natija.append('_')
        i += 1
    return "".join(natija)
print(pastki_chiziq_qoshish("amortizatsiya"))        


## 2. Integer Squares Exercise

n = int(input('n ni kiritng'))
for i in range(n):
    print(i ** 2)

## 3. Loop-Based Exercises
# Exercise 1: Print first 10 natural numbers using a while loop

i = 1
while i <= 10:
    print(i)
    i += 1

## Exercise 2: Print the following pattern

n = int(input("n ni kiriting: "))
for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

## Exercise 3: Calculate sum of all numbers from 1 to a given number

n = int(input("n ni kiriting: "))
yigindi = 0

for i in range(1, n+1):
    yigindi += i

print("Yig'indi:", yigindi)



n = int(input("n ni kiriting: "))
kupaytma = 1

for i in range(1, n+1):
    kupaytma *= i

print("ko'paytma:", kupaytma)


## Exercise 4: Print multiplication table of a given number

son = int(input("Son kiriting: "))

for i in range(1, 11):
    print(son * i)


## Exercise 5: Display numbers from a list using a loop

numbers = [12, 75, 150, 180, 145, 525, 50]
for son in numbers:
    sorted(numbers)
    print(son)


##  Exercise 6: Count the total number of digits in a number

son = int(input("Son kiriting: "))
raqamlar_soni = len(str(abs(son)))  
print("Raqamlar soni:", raqamlar_soni)


## Exercise 7: Print reverse number pattern

for i in range(10, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()


## Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50, 60, 70, 80]
for element in reversed(list1):
    print(element)


## Exercise 9: Display numbers from -10 to -1 using a for loop

for i in range(-10, 0):
    print(i)



## Exercise 10: Display message “Done” after successful loop execution

for i in range(15):
    print(i)
else:
    print("Done")



## Exercise 11: Print all prime numbers within a range

def tubmi(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

boshlangich = 25
oxirgi = 50

print(f"{boshlangich} dan {oxirgi} gacha bo‘lgan tub sonlar:")

for son in range(boshlangich, oxirgi + 1):
    if tubmi(son):
        print(son)


## Exercise 12: Display Fibonacci series up to 10 terms

n = 10

a, b = 0, 1
print("Fibonachchi ketma-ketligi:")

for _ in range(n):
    print(a, end='  ')
    a, b = b, a + b


## Exercise 13: Find the factorial of a given number

n = int(input("Son kiriting: "))

faktorial = 1
for i in range(1, n + 1):
    faktorial *= i

print(f"{n}! = {faktorial}")


## 4. Return Uncommon Elements of Lists

list1 = [10, 17, 20, 10]
list2 = [25, 30, 40,20]
def takrorbulmagan_elementlar(list1, list2):
    natija = []

    for elem in list1:
        if elem not in list2:
            natija.append(elem)

    for elem in list2:
        if elem not in list1:
            natija.append(elem)

    return natija
print(takrorbulmagan_elementlar(list1, list2))


