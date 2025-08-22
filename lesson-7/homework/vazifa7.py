## 1. is_prime(n) funksiyasi

def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

# Misol:
print(is_prime(4))  # False
print(is_prime(7))  # True


## 2. digit_sum(k) funksiyasi

def digit_sum(k):
    return sum(map(int, str(k)))

# Misol:
print(digit_sum(24))   # 6
print(digit_sum(502))  # 7


## 3. 2 ning darajalari (2**k), N dan oshmaydiganlar

def two_powers(N):
    k = 1
    while 2**k <= N:
        print(2**k, end=' ')
        k += 1
    print()

# Misol:
two_powers(10)  


def two_powers(N):
    k = 1
    while 5**k <= N:
        print(5**k, end=' ')
        k += 1
    print()

# Misol:
two_powers(525) 
