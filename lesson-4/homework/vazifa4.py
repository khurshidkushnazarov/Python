### 1. Sort a Dictionary by Value
## Write a Python script to sort (ascending and descending) a dictionary by value.
dict1 = {'a': 2, 'b': 3, 'c': 1, 'd': 4, 'e': 6, 'f':  5}

yangi = {}

for key, value in dict1.items():
    yangi[value] = key

dict1 = {}
yangi = dict(sorted(yangi.items()))

for key, value in yangi.items():
    dict1[value] = key
print(dict1)


## 2. Add a Key to a Dictionary
## Write a Python script to add a key to a dictionary.

my_dict = {'name': 'Khurshid','age': 39}
my_dict.update({"City":'Tashkent'})
print(my_dict)



## 3. Concatenate Multiple Dictionaries
## Write a Python script to concatenate the following dictionaries to create a new one.

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

merged_dict = {}
merged_dict.update(dict1)
merged_dict.update(dict2)
merged_dict.update(dict3)

print("Merged Dictionary:", merged_dict)


## 4. Generate a Dictionary with Squares
## Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n = int(input("enter number: "))
dict = {x: x*x for x in range(1, n+1)}
print("Dictionary of squares:", dict)


## 5. Dictionary of Squares (1 to 15)
## Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

dict = {x: x*x for x in range(1, 16)}
print("Dictionary of squares 1-15:", dict)


########### Set Exercises
## 1. Create a Set
## Write a Python program to create a set.

myset = {1,2,3,'lm','km'}
print("My_set:", myset)



## 2. Iterate Over a Set
## Write a Python program to iterate over sets.

my_set = {'olma', 'anor', 'gilos', 'nok','son','nok'}
print("set:")
for item in my_set:
    print(item)



## 3. Add Member(s) to a Set
## Write a Python program to add member(s) to a set.


my_set = {'olma', 'anor'}
my_set.add('gilos')
my_set.update(['son', 'kuchuk', 'ot'])
print("Updated set:", my_set)




## 4. Remove Item(s) from a Set
## Write a Python program to remove item(s) from a given set.

my_set: {'anor', 'gilos', 'son', 'olma', 'ot', 'kuchuk'}
my_set.remove('son')
print("Removed set:", my_set)



## 5. Remove an Item if Present in the Set
## Write a Python program to remove an item from a set if it is present in the set.

my_set = {'anor', 'gilos', 'son', 'olma', 'ot', 'kuchuk'}
item = 'otto'
if item in my_set:
    my_set.remove(item)
    print(f"'{item}' was removed from the set.")
else:
    print(f"'{item}' not found in the set.")
print("Updated set:", my_set)



## Kabisa yilimi?

year = int(input("Yilni kiriting: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} - Kabisa yili.")
else:
    print(f"{year} - oddiy yil.")
