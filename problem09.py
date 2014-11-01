#!/usr/bin/env python3
from functools import reduce
import operator

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a 

def pyth_triples(upper_bound,goal):
    for c in range(5,upper_bound+1):
        for b in range(4,c):
            for a in range(3,b):
                if(a*a + b*b == c*c and a+b+c == goal):
                    return([a,b,c])
                    
print(reduce(operator.mul, pyth_triples(1000,1000), 1))


        

