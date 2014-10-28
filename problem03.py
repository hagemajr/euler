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

def main():
    num = 600851475143
    low, high = 1, num
    prime_factors = []
    while(low < high):
        low += 1
        tmp = factor(low, num)
        if(tmp > 0):
            high = tmp
            if(is_prime(high)):
                prime_factors.append(high)
            if(is_prime(low)):
                prime_factors.append(low)
    print(max(prime_factors))            

main()