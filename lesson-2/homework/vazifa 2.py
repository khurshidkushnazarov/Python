## 1. Age Calculator
## Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
ism = input("Ismingizni kiriting: ")
tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: "))
yosh = 2025- tugilgan_yil
print(yosh)



## 2. Extract Car Names
## Extract car names from the following text:

txt = 'LMaasleitbtui'
print(txt[::2])
print(txt[1::2])


## 3. Extract Car Names
## Extract car names from the following text:
txt = 'MsaatmiazD'
print(txt[::2])
print(txt[-1:-10:-2])



## 4. Extract Residence Area
## Extract the residence area from the following text:

txt = "I'am John. I am from London"
print(txt[20::])



## 5. Reverse String
## Write a Python program that takes a user input string and prints it in reverse order.


txt = "London"
print(txt[::-1])


## 6. Count Vowels
## Write a Python program that counts the number of vowels in a given string.

txt = input("so'zni kiriting")
unlilar = "aeiouAEIOU"
count = txt.count('a') + txt.count('e') + txt.count('i') + txt.count('o') + txt.count('u') + \
        txt.count('A') + txt.count('E') + txt.count('I') + txt.count('O') + txt.count('U')

print("Unli harflar soni:", count)


## 7. Find Maximum Value
## Write a Python program that takes a list of numbers as input and prints the maximum value.

list = [1,12,3,24,5]
maksimal_son = max(list)
print("eng katta son: ", maksimal_son)



## 8. Check Palindrome
## Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

soz = "anna"
if soz == soz[::-1]:
    print("Bu so'z palindrom.")
else:
    print("Bu so'z palindrom emas.")



## 9. Extract Email Domain
## Write a Python program that extracts and prints the domain from an email address provided by the user.

email = input("Email manzilingizni kiriting")
domen = email.split('@')[-1]
print(domen)


## 10. Generate Random Password
## Write a Python program to generate a random password containing letters, digits, and special characters.
import random
parollar ="QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()"
parol = ''.join(random.choices(parollar, k=10))
print(parol)
