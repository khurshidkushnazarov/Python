# 1. Convert List to 1D Array
# Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

#   Expected Output:
# Original List: [12.23, 13.32, 100, 36.32] One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]

import numpy as np

list_of_numbers = [1.1, 2, 3, 4, 5.6]
array_1d = np.array(list_of_numbers)
print("1D NumPy массив:", array_1d)


# 2. Create 3x3 Matrix (2?10)
# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

import numpy as np

numbers = np.arange(2, 11)  # 11 дан олдинги сонларгача (2,...,10)
matrix_3x3 = numbers.reshape((3, 3))
print(matrix_3x3)

# 3. Null Vector (10) & Update Sixth Value
# Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

# [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# Update sixth value to 11 [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]

import numpy as np

vector = np.zeros(10)
print("Бошланғич вектор:")
print(vector)

vector[6] = 11
print("\nОлтинчи қиймат янгилангандан кейин:")
print(vector)


# 4. Array from 12 to 38
# Write a NumPy program to create an array with values ranging from 12 to 38.

# Expected Output:
# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

import numpy as np

array = np.arange(12, 38)
print(array)


# 5. Convert Array to Float Type
# Write a NumPy program to convert an array to a floating type.

# Sample output:
# Original array [1, 2, 3, 4]

import numpy as np

array = np.array([1, 2, 3, 4])
float_array = array.astype(float)

print("Асосий массив:", array)
print("Ўнлик турига айланган массив:", float_array)

# 6. Celsius to Fahrenheit Conversion
# Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.
# Sample Array [0, 12, 45.21, 34, 99.91] [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]
# Expected Output:
# Values in Fahrenheit degrees: [ 0. 12. 45.21 34. 99.91 32. ]
# Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]
# Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]
# Values in Fahrenheit degrees: [-0. 12. 45.21 34. 99.91 32. ]

import numpy as np

celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = (celsius * 9/5) + 32

print("Цельсий даражаларидаги қийматлар:", celsius)
print("Фаренгейт даражаларидаги қийматлар:", fahrenheit)


# 7. Append Values to Array (Do self-tudy)
# Write a NumPy program to append values to the end of an array.

# Expected Output:
# Original array: [10, 20, 30]
# After append values to the end of the array: [10 20 30 40 50 60 70 80 90]

import numpy as np

array = np.array([10, 20, 30])
print("Асосий массив:", array)

values_to_add = np.array([40, 50, 60, 70, 80, 90])

new_array = np.append(array, values_to_add)

print("Қийматлар қўшилгандан кейин:", new_array)



# 8. Array Statistical Functions (Do self-tudy)
# Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.

import numpy as np

array = np.random.randint(0, 101, size=10)
print("Тасодифий массив:", array)

mean_value = np.mean(array)

median_value = np.median(array)

std_deviation = np.std(array)

print(f"Ўртача қиймат: {mean_value}")
print(f"Медиана: {median_value}")
print(f"Стандарт четлашув: {std_deviation}")


# 9 Find min and max
# Create a 10x10 array with random values and find the minimum and maximum values.

import numpy as np

array = np.random.randint(0, 101, size=(10, 10))
print("Тасодифий 10x10 массив:\n", array)

min_value = np.min(array)

max_value = np.max(array)

print(f"Энг кичик қиймат: {min_value}")
print(f"Энг катта қиймат: {max_value}")


# 10.Create a 3x3x3 array with random values.

import numpy as np

array_3d = np.random.randint(0, 101, size=(3, 3, 3))
print("3x3x3 ўлчамли тасодифий массив:\n", array_3d)
