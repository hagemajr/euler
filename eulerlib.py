#!/usr/bin/env python3
def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def factor(num1, num2):
    if(num2 % num1 == 0):
        return num2 / num1
    else:
        return 0
