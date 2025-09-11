# 1.Task: JSON Parsing
# write a Python script that reads the students.jon JSON file and prints details of each student.

import json

with open('students.json', 'r', encoding='utf-8') as file:
    students = json.load(file)

for i, student in enumerate(students, start=1):
    print(f"Талаба {i}:")
    print(f"  Исм: {student['ism']}")
    print(f"  Фамилия: {student['фамилия']}")
    print(f"  Ёши: {student['ёши']}")
    print(f"  Курс: {student['курс']}")
    print()



# 2.Task: Weather API
# Use this url : https://openweathermap.org/
# Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).


import requests

API_KEY = '3882d5ae8b9e5c850ae6907f3c0ab3f8' 
CITY = 'Tashkent'
URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=uz'

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    
    shahar = data['name']
    harorat = data['main']['temp']
    namlik = data['main']['humidity']
    bosim = data['main']['pressure']
    tavsif = data['weather'][0]['description']
    
    print(f" Об-ҳаво маълумоти — {shahar}:")
    print(f"  - Ҳарорат: {harorat}°C")
    print(f"  - Намлик: {namlik}%")
    print(f"  - Босим: {bosim} hPa")
    print(f"  - Ҳолат: {tavsif}")
else:
    print(" Маълумотни олишда хатолик юз берди.")
    print(f"Код: {response.status_code} — {response.text}")


# 3.Task: JSON Modification
# Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.

import json
import os

FILENAME = 'books.json'

def load_books():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_books(books):
    with open(FILENAME, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

def add_book():
    books = load_books()
    new_id = max([book['id'] for book in books], default=0) + 1
    nomi = input("Китоб номи: ")
    muallif = input("Муаллиф: ")
    yil = int(input("Нашр йили: "))
    
    books.append({
        "id": new_id,
        "nomi": nomi,
        "muallif": muallif,
        "yil": yil
    })
    save_books(books)
    print(" Китоб қўшилди.")

def update_book():
    books = load_books()
    book_id = int(input("Янгилаш учун китоб ID: "))
    
    for book in books:
        if book['id'] == book_id:
            print(f"Топилди: {book['nomi']} ({book['muallif']}, {book['yil']})")
            book['nomi'] = input("Янги номи: ") or book['nomi']
            book['muallif'] = input("Янги муаллиф: ") or book['muallif']
            yil_input = input("Янги нашр йили: ")
            if yil_input:
                book['yil'] = int(yil_input)
            save_books(books)
            print(" Китоб маълумотлари янгиланди.")
            return
    print(" Бу ID билан китоб топилмади.")

def delete_book():
    books = load_books()
    book_id = int(input("Ўчириш учун китоб ID: "))
    new_books = [book for book in books if book['id'] != book_id]
    
    if len(new_books) != len(books):
        save_books(new_books)
        print(" Китоб ўчирилди.")
    else:
        print(" Бу ID билан китоб топилмади.")

def main():
    while True:
        print("\n Китоблар билан ишлаш тизими")
        print("1. Янги китоб қўшиш")
        print("2. Китоб маълумотини таҳрирлаш")
        print("3. Китобни ўчириш")
        print("4. Чиқиш")

        choice = input("Танловни киритинг (1-4): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            print(" Дастур тугади.")
            break
        else:
            print(" Нотўғри танлов. Қайта уриниб кўринг.")

if __name__ == "__main__":
    main()


# 4.Task: Movie Recommendation System
# Use this url http://www.omdbapi.com/ to fetch information about movies.
# Create a program that asks users for a movie genre and recommends a random movie from that genre.

import requests
import random

API_KEY = '8e689a69-6f34-4091-a111-995a80261861'

def get_movies_by_genre(genre):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&type=movie&s={genre}"
    response = requests.get(url)
    if response.status_code != 200:
        print("API билан боғланишда хатолик юз берди.")
        return []
    data = response.json()
    if data.get('Response') == 'False':
        print(f"Фильм топилмади: {data.get('Error')}")
        return []
    return data.get('Search', [])

def get_movie_details(imdb_id):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&i={imdb_id}&plot=short"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

def main():
    genre = input("Қайси жанрда фильм керак? (масалан: Action, Comedy, Drama): ").strip()

    movies = get_movies_by_genre(genre)

    if not movies:
        print("Кечирасиз, шу жанрда фильм топилмади.")
        return

    movie = random.choice(movies)
    details = get_movie_details(movie['imdbID'])

    if details:
        print("\n Тасодифий фильм тавсияси:")
        print(f"Номи: {details.get('Title')}")
        print(f"Жанр: {details.get('Genre')}")
        print(f"Йил: {details.get('Year')}")
        print(f"Рейтинг: {details.get('imdbRating')}")
        print(f"Қисқача маълумот: {details.get('Plot')}")
        print(f"IMDb URL: https://www.imdb.com/title/{details.get('imdbID')}/")
    else:
        print("Фильм ҳақида маълумот олиш мумкин эмас.")

if __name__ == "__main__":
    main()
