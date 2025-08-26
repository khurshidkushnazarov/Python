## 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting: "))
    natija = a / b
    print("Natija:", natija)
except ZeroDivisionError:
    print("Xatolik: Nolga bo‘lish mumkin emas!")

## 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

yosh = input("Yoshingizni kiriting: ")
try:
    yosh = int(yosh)
except:
    print('Siz butun son kiritmadingiz')
else:
    print(f"Siz {2025-yosh} yilda tug'ilgansiz")

## 3.Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

try:
    with open ('xlzz.txt', 'r') as f:
        data = f.read(11)
        f.seek(0)
except:
    print('Fayl topilmadi')
else:
    print(data)



## 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

try:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting: "))
    natija = a / b
    print("Natija:", natija)
except:
    print("Xatolik: Siz son kiritmadingiz!")

## 5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

filename = 'xurshid.txt'
try:
    with open(filename,'r') as f:
        data = f.read()
except PermissionError:
    print(f"Xatolik: '{filename}' faylini o‘qish uchun ruxsat yo‘q.")
except FileNotFoundError:
    print(f"Xatolik: '{filename}' fayli topilmadi.")        
else:
    print("Fayldan o‘qilgan ma’lumot:")
    print(data)


## 6.Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

mylist = [1, 2, 3, 4, 5]

try:
    index = int(input("Qaysi indeksdagi elementni ko‘rmoqchisiz? "))
    element = mylist[index]
except IndexError:
    print("Xatolik: Kiritilgan indeks ro‘yxat chegarasidan tashqarida!")
except ValueError:
    print("Xatolik: Iltimos, butun son kiriting!")
else:
    print(f"Ro‘yxatdagi {index}-indeksdagi element: {element}")


mylist = ['Sarvar','Anvar','Ali']
try:
    index = int(input("Qaysi indeksdagi elementni ko‘rmoqchisiz? "))
    element = mylist[index]
except IndexError:
    print("Xatolik: Kiritilgan indeks ro‘yxat chegarasidan tashqarida!")
except ValueError:
    print("Xatolik: Iltimos, butun son kiriting!")
else:
    print(f"Ro‘yxatdagi {index}-indeksdagi element: {element}")


7. ## Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.

try:
    number = int(input("Biror butun son kiriting"))
except KeyboardInterrupt:
    print("\nKiritish bekor qilindi (KeyboardInterrupt).")
except ValueError:
    print("Xatolik: Iltimos, butun son kiriting!")
else:
    print(f"Siz kiritgan son:{number}")

## 8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
try:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting: "))
    natija = a / b
except ArithmeticError:
    print("Xatolik: Arifmetik xatolik yuz berdi (masalan, nolga bo‘lish).")
except ValueError:
    print("Xatolik: Iltimos, son kiriting!")
else:
    print("Natija:", natija)


## 9.Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

filename = 'xurshid.txt'
try:
    with open(filename,'r', encoding='utf-8') as f:
        data = f.read()
except UnicodeDecodeError:
    print(f"Xatolik: '{filename}' faylini UTF-8 kodlashda o‘qib bo‘lmadi. Kodlash mos emas.")
except FileNotFoundError:
    print(f"Xatolik: '{filename}' fayli topilmadi.")        
else:
    print("Fayldan o‘qilgan ma’lumot:")
    print(data)

## 10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

mylist = [1, 2, 3, 4, 5]

try:
    mylist.push(6)
except AttributeError:
    print("Xatolik: Ro‘yxatda mavjud bo‘lmagan atribut yoki metodga murojaat qilindi.")
else:
    print("Element muvaffaqiyatli qo‘shildi.")



mylist = [1, 2, 3, 4, 'Ali']

try:
    mylist.size(6)
except AttributeError:
    print("Xatolik: Ro‘yxatda mavjud bo‘lmagan atribut yoki metodga murojaat qilindi.")
else:
    print("Element muvaffaqiyatli qo‘shildi.")





##Python File Input Output: Exercises, Practice, Solution
##File Input/Output Exercises
## 1.Write a Python program to read an entire text file.

filename = 'xurshid.txt'
with open(filename,'r') as f:
    data = f.read()
    print(data)



## 2.Write a Python program to read first n lines of a file.
filename = 'xurshid.txt'
with open(filename,'r') as f:
    data = f.read(16)
    print(data)


## 2.Write a Python program to read first n lines of a file.
filename = 'xurshid.txt'

try:
    n = int(input("Nechta birinchi qatordan o‘qimoqchisiz? "))
    with open(filename, 'r', encoding='utf-8') as f:
        for i in range(n):
            line = f.readline()
            if not line:
                break 
            print(line.strip())
except FileNotFoundError:
    print(f"Xatolik: '{filename}' fayli topilmadi.")
except ValueError:
    print("Xatolik: Iltimos, butun son kiriting!")


## 3.Write a Python program to append text to a file and display the text.
filename = 'xurshid.txt'
try:
    user_text = input("Faylga qo‘shmoqchi bo‘lgan matnni kiriting: ")

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(user_text + '\n')

    print("\nFayldagi joriy matn:")
    with open(filename, 'r', encoding='utf-8') as f:
        contents = f.read()
        print(contents)

except Exception as e:
    print(f"Xatolik yuz berdi: {e}")


## 4.Write a Python program to read last n lines of a file.

filename = 'xurshid.txt'

try:
    n = int(input("Oxiridan nechta qatordan o‘qimoqchisiz? "))

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()  
        
    last_lines = lines[-n:]

    print(f"\nFaylning oxirgi {n} qatori:")
    for line in last_lines:
        print(line.strip())

except FileNotFoundError:
    print(f"Xatolik: '{filename}' fayli topilmadi.")
except ValueError:
    print("Xatolik: Iltimos, butun son kiriting!")
except Exception as e:
    print(f"Kutilmagan xatolik: {e}")


## 5.Write a Python program to read a file line by line and store it into a list.

filename = 'xurshid.txt'
try:
    with open(filename, 'r', encoding='utf-8') as f:
        lines_list = [line.strip() for line in f] 
    print("Fayl ro‘yxat ko‘rinishida:")
    print(lines_list)

except FileNotFoundError:
    print(f"Xatolik: '{filename}' fayli topilmadi.")
except Exception as e:
    print(f"Kutilmagan xatolik: {e}")


## 6.Write a Python program to read a file line by line and store it into a variable.
filename = 'xurshid.txt'
try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = ""
        for line in f:
            content += line

    print("Fayldagi matn:")
    print(content)


except FileNotFoundError:
    print(f"Xatolik: '{filename}' fayli topilmadi.")
except Exception as e:
    print(f"Kutilmagan xatolik: {e}")


filename = 'xurshid.txt'
with open(filename, 'r', encoding='utf-8') as f:
    content = ""
    for line in f:
        content += line

    print("Fayldagi matn:")
    print(content)


## 7.Write a Python program to read a file line by line and store it into an array.

filename = 'xurshid.txt'
try:
    with open(filename, 'r', encoding='utf-8') as f:
        array = [line.strip() for line in f]

    print("Fayl ma'lumotlari ro‘yxat (list) ko‘rinishida:")
    print(array)

except FileNotFoundError:
    print(f"Xatolik: '{filename}' fayli topilmadi.")
except Exception as e:
    print(f"Kutilmagan xatolik: {e}")


## 8.Write a Python program to find the longest words.

text = input("Matn kiriting: ")
words = text.split()
max_len = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_len]

print(f"Eng uzun so‘z(lar) (uzunligi {max_len}):")
print(longest_words)


## 9.Write a Python program to count the number of lines in a text file.

filename = 'xurshid.txt'
try:
    with open(filename, 'r', encoding='utf-8') as f:
        line_count = sum(1 for _ in f)

    print(f"Fayldagi qatorlar soni: {line_count}")

except FileNotFoundError:
    print(f"Xatolik: '{filename}' fayli topilmadi.")
except Exception as e:
    print(f"Kutilmagan xatolik: {e}")


## 10.Write a Python program to count the frequency of words in a file.

from collections import Counter
import re
filename = 'xurshid.txt'

try:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()

    words = re.findall(r'\b\w+\b', text)

    word_counts = Counter(words)

    print("Fayldagi so‘zlar chastotasi:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

except FileNotFoundError:
    print(f"Xatolik: '{filename}' fayli topilmadi.")
except Exception as e:
    print(f"Kutilmagan xatolik: {e}")



## 11.Write a Python program to get the file size of a plain file.

import os
file_path = 'xurshid.txt'
file_size = os.path.getsize(file_path)
print(f"File size: {file_size} bytes")


## 12.Write a Python program to write a list to a file.

data = ['apple', 'banana', 'cherry']

with open('fruits.txt', 'w') as file:
    for item in data:
        file.write(item + '\n')

## 13.Write a Python program to copy the contents of a file to another file.

with open('fruits.txt', 'r') as src, open('xxz.txt', 'w') as dest:
    dest.write(src.read())


## 14.Write a Python program to combine each line from the first file with the corresponding line in the second file.

with open('fruits.txt', 'r') as f1, open('xxz.txt', 'r') as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())


## 15. Write a Python program to read a random line from a file.

import random

with open('fruits.txt', 'r') as file:
    lines = file.readlines()
    print(random.choice(lines).strip())


## 16.Write a Python program to assess if a file is closed or not.

file = open('fruits.txt', 'r')
print("Closed?", file.closed)
file.close()
print("Closed?", file.closed)


### 17. Write a Python program to remove newline characters from a file.

input_filename = 'xz.txt'   
output_filename = 'xs.txt'

with open(input_filename, 'r', encoding='utf-8') as infile:
    content = infile.read()

content_without_newlines = content.replace('\n', '')

with open(output_filename, 'w', encoding='utf-8') as outfile:
    outfile.write(content_without_newlines)

print(f"Янги қатор белгиларисиз матн '{output_filename}' файлига ёзилди.")


## 18.Write a Python program that takes a text file as input and returns the number of words in a given text file.
## Note: Some words can be separated by a comma with no space.

import re

def count_words_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    words = re.findall(r'\b\w+\b', text)
    
    return len(words)

input_filename = 'xs.txt'

word_count = count_words_in_file(input_filename)
print(f"Файлдаги сўзлар сони: {word_count}")

## 19.Write a Python program to extract characters from various text files and put them into a list.


def collect_characters_from_files(filenames):
    characters = []
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            characters.extend(content)
    return characters

files = ['fr.txt', 'cars.txt']

all_characters = collect_characters_from_files(files)
print(all_characters)
print(f"Жами белгилар сони: {len(all_characters)}")


## 20. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
import string

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Бу {filename} файли.\n")

print("Файллар яратилди!")


## 21.Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.

import string

def write_alphabet_repeated(filename, repeat_count):
    with open(filename, 'w', encoding='utf-8') as file:
        for letter in string.ascii_uppercase:  # A dan Z gacha
            file.write(letter * repeat_count + '\n')

output_file = 'alphabet.txt'
repeat_number = 10 

write_alphabet_repeated(output_file, repeat_number)
print(f"'{output_file}' файли яратилди, ҳар бир ҳарф {repeat_number} марта такрорланган ҳолда.")


