# Homework:

# 1.Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.

from datetime import datetime
from dateutil.relativedelta import relativedelta

def main():
    
    birth_date_str = input("Туғилган санангизни киритинг (ЙЙЙЙ-ОЙ-КУН форматида): ")

    try:
       
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
        today = datetime.today().date()

        if birth_date > today:
            print("Хатолик: туғилган сана келажакда бўлиши мумкин эмас.")
            return
      
        age = relativedelta(today, birth_date)

        print(f"\nСизнинг ёшингиз: {age.years} йил, {age.months} ой, {age.days} кун.")

    except ValueError:
        print("Илтимос, санани тўғри форматда киритинг (ЙЙЙЙ-ОЙ-КУН).")

if __name__ == "__main__":
    main()



# 2.Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

from datetime import datetime, date

def days_until_next_birthday(birth_date):
    today = date.today()
    current_year = today.year

 
    next_birthday = birth_date.replace(year=current_year)
    
    if next_birthday < today:
        next_birthday = birth_date.replace(year=current_year + 1)

    delta = next_birthday - today
    return delta.days

def main():
    birth_str = input("Туғилган санангизни киритинг (ЙЙЙЙ-ОЙ-КУН): ")

    try:
        birth_date = datetime.strptime(birth_str, "%Y-%m-%d").date()
        days_left = days_until_next_birthday(birth_date)

        if days_left == 0:
            print("Тугилган кунингиз муборак! Бугун сизнинг туғилган кунингиз.")
        else:
            print(f"Келаси туғилган кунигача {days_left} кун қолди.")

    except ValueError:
        print("Илтимос, санани тўғри форматда киритинг (ЙЙЙЙ-ОЙ-КУН).")

if __name__ == "__main__":
    main()



# 3.Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.


from datetime import datetime, timedelta

def main():
        start_str = input("Жорий сана ва вақтни киритинг (ЙЙЙЙ-ОЙ-КУН СОАТ:ДАҚИҚА): ")

    try:
        start_time = datetime.strptime(start_str, "%Y-%m-%d %H:%M")

       
        hours = int(input("Учрашув давомийлиги (соат): "))
        minutes = int(input("Учрашув давомийлиги (дақиқа): "))

        
        duration = timedelta(hours=hours, minutes=minutes)

        
        end_time = start_time + duration

        print(f"\nУчрашув {end_time.strftime('%Y-%m-%d %H:%M')} да тугайди.")

    except ValueError:
        print("Илтимос, санани ва вақтни тўғри форматда киритинг.")

if __name__ == "__main__":
    main()


# 4.Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.

from datetime import datetime
from zoneinfo import ZoneInfo

def main():
   
    dt_str = input("Сана ва вақтни киритинг (ЙЙЙЙ-ОЙ-КУН СОАТ:ДАҚИҚА): ")
    from_tz_str = input("Жорий вақт зонасини киритинг (масалан, Asia/Tashkent): ")
    to_tz_str = input("Айлантириш керак бўлган вақт зонасини киритинг (масалан, Europe/Moscow): ")

    try:
        
        naive_dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")

       
        from_tz = ZoneInfo(from_tz_str)
        to_tz = ZoneInfo(to_tz_str)

        
        aware_dt = naive_dt.replace(tzinfo=from_tz)

    
        converted_dt = aware_dt.astimezone(to_tz)

        print(f"\n{from_tz_str} вақти: {aware_dt.strftime('%Y-%m-%d %H:%M %Z%z')}")
        print(f"{to_tz_str} вақтига айлантирилган: {converted_dt.strftime('%Y-%m-%d %H:%M %Z%z')}")

    except Exception as e:
        print("Хатолик: Илтимос, маълумотларни тўғри киритинг.")
        print(f"Қўшимча маълумот: {e}")

if __name__ == "__main__":
    main()


# 5. Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).

from datetime import datetime
import time
import os
import sys

def clear_screen():
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    target_str = input("Муддатни киритинг (ЙЙЙЙ-ОЙ-КУН СОАТ:ДАҚИҚА:СОНИЯ), масалан: 2025-12-31 23:59:59: ")

    try:
        target_time = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")

        while True:
            now = datetime.now()
            remaining = target_time - now

            if remaining.total_seconds() <= 0:
                clear_screen()
                print(" Белгиланган вақт етиб келди!")
                break

            days = remaining.days
            hours, remainder = divmod(remaining.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            clear_screen()
            print("⏳ Қолган вақт:")
            print(f"{days} кун, {hours:02d} соат, {minutes:02d} дақиқа, {seconds:02d} сония")

            time.sleep(1)

    except ValueError:
        print(" Формат хато! Илтимос, санани тўғри форматда киритинг.")

if __name__ == "__main__":
    main()

# 6.Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.

import re

def is_valid_email(email):
   
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def main():
    email = input("Электрон почта манзилини киритинг: ")

    if is_valid_email(email):
        print(" Манзил формати тўғри.")
    else:
        print(" Манзил формати нотўғри. Масалан: ism@example.com")

if __name__ == "__main__":
    main()

#7.Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".

def format_phone_number(phone):
    
    digits = ''.join(filter(str.isdigit, phone))

 
    if len(digits) != 10:
        return None
   
    area = digits[:3]
    middle = digits[3:6]
    last = digits[6:]
    return f"({area}) {middle}-{last}"

def main():
    phone_input = input("Телефон рақамини киритинг (фақат рақамлар, масалан: 998901234567 ёки 901234567): ")

    formatted = format_phone_number(phone_input)

    if formatted:
        print(" Форматланган рақам:", formatted)
    else:
        print(" Нотўғри рақам! Илтимос, 10 та рақам киритинг.")

if __name__ == "__main__":
    main()

# 8. Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).

import re

def check_password_strength(password):
    errors = []

   
    if len(password) < 8:
        errors.append("Пароль камида 8 та белгидан иборат бўлиши керак.")

    
    if not re.search(r'[a-z]', password):
        errors.append("Пароль камида битта кичик ҳарф (a–z) бўлиши керак.")

    
    if not re.search(r'[A-Z]', password):
        errors.append("Пароль камида битта катта ҳарф (A–Z) бўлиши керак.")

    
    if not re.search(r'[0-9]', password):
        errors.append("Пароль камида битта рақам (0–9) бўлиши керак.")

    return errors

def main():
    password = input("Паролни киритинг: ")
    errors = check_password_strength(password)

    if not errors:
        print(" Парол мустаҳкам!")
    else:
        print(" Парол заиф. Сабаблари:")
        for err in errors:
            print("-", err)

if __name__ == "__main__":
    main()


#9.Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

def find_word(text, word):
    word_lower = word.lower()
    text_lower = text.lower()

    count = 0
    positions = []

    index = text_lower.find(word_lower)
    while index != -1:
        count += 1
        positions.append(index)
        index = text_lower.find(word_lower, index + 1)

    return count, positions

def main():
    text = input("Матнни киритинг:\n")
    word = input("\nҚидириладиган сўзни киритинг: ")

    count, positions = find_word(text, word)

    if count > 0:
        print(f"\n Сўз '{word}' {count} марта учради.")
        print(" Индекс(лар):", positions)
    else:
        print(f"\n Сўз '{word}' матнда топилмади.")

if __name__ == "__main__":
    main()

# 10.Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.

import re

def extract_dates(text):
   
    date_patterns = [
        r"\b\d{4}-\d{2}-\d{2}\b",
        r"\b\d{2}/\d{2}/\d{4}\b",
        r"\b\d{2}\.\d{2}\.\d{4}\b",
    ]

    found_dates = []
    for pattern in date_patterns:
        matches = re.findall(pattern, text)
        found_dates.extend(matches)

    return found_dates

def main():
    text = input("Матнни киритинг:\n")
    dates = extract_dates(text)

    if dates:
        print("\n Матнда топилган саналар:")
        for date in dates:
            print("-", date)
    else:
        print("\n Матнда бирор сана топилмади.")

if __name__ == "__main__":
    main()

