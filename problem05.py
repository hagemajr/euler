#!/usr/bin/env python3
from functools import reduce
import operator
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

def smallest_multiple(multiples):
    #we'll be making a table, one row per multipler, one column per prime that divides into it
    table = dict()
    primes = [x for x in range(min(multiples),max(multiples)+1) if is_prime(x)]
    
    #loop through each multiplier
    for x in multiples:
        cols, val, remainder = [],0,0
        #loop through each prime, keeping track of how many times it divides in cleanly
        for y in primes:
            val = x
            while(val != 1):
                if(val % y == 0):
                    val = val / y
                    cols.append(y)
                else:
                    val = 1
        #we're all done, this is our row
        table[x] = cols
    cols = []
    #now, we need to find the common items in each row, to build the column headers
    for k,v in table.items():
        col_set = list(set(v))
        for x in col_set:
            if(cols.count(x) != v.count(x)):
                for y in range(1, v.count(x) - cols.count(x) + 1):
                    cols.append(x)
    #multiply the column header to find the least common multiple
    return reduce(operator.mul, cols, 1)
 

start_time = time.time()
print(smallest_multiple(range(1,101)))
print("Execution time: {0}".format(time.time() - start_time))     
            
            