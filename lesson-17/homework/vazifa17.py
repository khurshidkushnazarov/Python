# Homework 1:

import pandas as pd
import numpy as np

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

df.rename(columns=lambda x: x.lower().replace(" ", "_"), inplace=True)


print("Биринчи 3 қатор:")
print(df.head(3))

mean_age = df["age"].mean()
print(f"\nЎртача ёш: {mean_age}")

print("\nИсм ва шаҳарлар:")
print(df[['first_name', 'city']])

df['salary'] = np.random.randint(4000, 10000, size=len(df))

print("\nУмумий статистика:")
print(df.describe())

# Homework 2:

sales_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(sales_data)

print("Максимум сoтиш:", sales_and_expenses['Sales'].max())
print("Максимум харажат:", sales_and_expenses['Expenses'].max())

print("Минимум сoтиш:", sales_and_expenses['Sales'].min())
print("Минимум харажат:", sales_and_expenses['Expenses'].min())

print("Ўртача сoтиш:", sales_and_expenses['Sales'].mean())
print("Ўртача харажат:", sales_and_expenses['Expenses'].mean())

# Homework 3:

expenses_data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(expenses_data)

expenses.set_index('Category', inplace=True)


print("Максимум харажатлар:")
print(expenses.max(axis=1))


print("\nМинимум харажатлар:")
print(expenses.min(axis=1))


print("\nЎртача харажатлар:")
print(expenses.mean(axis=1))
