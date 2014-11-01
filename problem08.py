#!/usr/bin/env python3
from functools import reduce
import operator

f = open('problem08.txt', 'r')
num = f.read()
f.close()

digits = []
literals = []
max_product = 0

for x in range(0,988):
    if(reduce(operator.mul, map(int, num[x:x+13]), 1) > max_product):
        digits = map(int, num[x:x+13])
        max_product = reduce(operator.mul, digits, 1)
        literals = num[x:x+13]

print("The maximum product is {0} which is made from the following digits: ".format(max_product))
print(literals)