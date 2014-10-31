#!/usr/bin/env python3
import time

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

start_time = time.time()
counter = 1
increment_me = 1
while(counter != 10001):
    increment_me += 2
    if(is_prime(increment_me)):
        counter += 1
print(increment_me)
print("Execution time: {0}".format(time.time() - start_time))

