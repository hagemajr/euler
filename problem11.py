#!/usr/bin/env python3
file = open('problem11.txt','r')
idx = 0
table = dict()
for line in file:
    table[idx] = str.split(line)
    idx += 1
file.close()

def up_down_products(table, depth):
    #product = table[0][0] * table[1][0] * table[2][0] * table[3][0]
    max_product = 1
    product = 1
    height = max(table.keys())
    width = len(table[0]) - 1
    for x in range(0,height):
        for y in range(0,width):
            for z in range(0,depth):
                if(x+z > height or y+z > width):
                    product = 1
                    break
                else:
                    product *= int(table[x+z][y])
            if(product > max_product):
                max_product = product
            product = 1
        product = 1
    return max_product

def left_right_products(table, num):
    #product = table[0][0] * table[0][1] * table[0][2] * table[0][3]
    max_product = 1
    product = 1
    height = max(table.keys())
    width = len(table[0]) - 1
    for x in range(0,height):
        for y in range(0,width):
            for z in range(0,4):
                if(x+z > height or y+z > width):
                    product = 1
                    break
                else:
                    product *= int(table[x][y+z])
            if(product > max_product):
                max_product = product
            product = 1
        product = 1
    return max_product

def diagonal_products(table, num):
    #product = table[0][0] * table [1][1] * table[2][2] * table[3][3]
    #product = table[0][19] * table[1][18] * table[2][17] * table [3][16]
    max_product = 1
    product = 1
    height = max(table.keys())
    width = len(table[0]) - 1
    for x in range(0,height):
        for y in range(0,width):
            for z in range(0,4):
                if(x+z > height or y+z > width):
                    product = 1
                    break
                else:
                    product *= int(table[x+z][y+z])
            if(product > max_product):
                max_product = product
            product = 1
        product = 1
    product = 1
    for x in range(height,0,-1):
        for y in range(width,0,-1):
            for z in range(0,4):
                if(x+z > height or y-z < 0):
                    product = 1
                    break
                else:
                    product *= int(table[x+z][y-z])
            if(product > max_product):
                max_product = product
            product = 1
        product = 1
    return max_product
    
products = [up_down_products(table,4), left_right_products(table,4), diagonal_products(table,4)]
print(max(products))