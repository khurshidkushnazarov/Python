# Exercise 1: Threaded Prime Number Checker
# Write a Python program that checks whether a given range of numbers contains prime numbers. Divide the range among multiple threads to parallelize the prime checking process. Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.

import threading


prime_numbers = []
lock = threading.Lock()  

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_primes_in_range(start, end):
    local_primes = []
    for num in range(start, end):
        if is_prime(num):
            local_primes.append(num)
    with lock:
        prime_numbers.extend(local_primes)

def main():
    start_range = 1
    end_range = 100
    thread_count = 4 

    threads = []
    step = (end_range - start_range) // thread_count

    for i in range(thread_count):
        start = start_range + i * step
        
        end = start_range + (i + 1) * step if i != thread_count - 1 else end_range
        t = threading.Thread(target=check_primes_in_range, args=(start, end))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Топилган содда сонлар:")
    print(sorted(prime_numbers))

if __name__ == "__main__":
    main()



# Exercise 2: Threaded File Processing

# Write a program that reads a large text file containing lines of text. Implement a threaded solution to count the occurrence of each word in the file. Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.


import threading
from collections import Counter


word_counts = Counter()
lock = threading.Lock()


def process_lines(lines):
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        words = [word.strip('.,!?;:()"\'').lower() for word in words if word]
        local_counter.update(words)
    with lock:
        word_counts.update(local_counter)


def main():
    filename = 'suzlar.txt' 
    thread_count = 4 

  
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    step = total_lines // thread_count
    threads = []

    for i in range(thread_count):
        start = i * step
        end = (i + 1) * step if i != thread_count - 1 else total_lines
        t = threading.Thread(target=process_lines, args=(lines[start:end],))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

      print("Сўзлар сони:")
    for word, count in word_counts.most_common():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
