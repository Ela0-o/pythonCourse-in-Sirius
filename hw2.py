import math as m


def is_prime(c):
    if isinstance(c, int) and c > 0:
        if c < 2:
            return False
        for i in range(2, int(m.sqrt(c))+1):
            if c % i == 0:
                return False
        else:
            return True
    else:
        raise AssertionError
# def is_prime(c):
#     if isinstance(c, int) and c > 0:
#         if c < 2:
#             return False
#         for i in range(2, c + 1):
#             if c % i == 0 and c != i:
#                 return False
#             elif c % i == 0 and c == i:
#                 return True
#     else:
#         raise AssertionError


def next_prime(a):
    if isinstance(a, int) and a > 0:
        if a > 2:
            b = a
            while True:
                if is_prime(b) and b >= a:
                    return b
                else:
                    b += 1
        else:
            return 2
    else:
        raise AssertionError


# def print_all_primes():
#     n = 1
#     while(True):
#         if is_prime(n):
#             print(n)
#         n += 1

def gcd(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise AssertionError
    a = abs(a)
    b = abs(b)
    if a == 0 or b == 0:
        return max(a, b)
    gcd_meaning = 1
    a_fact = a
    b_fact = b
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0 and is_prime(i):
            while a_fact % i == 0 and b_fact % i == 0:
                gcd_meaning *= i
                a_fact //= i
                b_fact //= i
    return gcd_meaning


def are_coprime(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise AssertionError
    a = abs(a)
    b = abs(b)
    if gcd(a, b) == 1:
        return True
    return False

# print(is_prime(25))

