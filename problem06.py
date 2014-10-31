#!/usr/bin/env python3

list_of_nums = range(1,101)

sum_of_squares = sum([x**2 for x in list_of_nums])
square_of_sum = sum(list_of_nums)**2
print(square_of_sum - sum_of_squares)