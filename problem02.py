#!/usr/bin/python3.4

def main():
    a = 1
    b = 2
    fib = []
    even_fib = []
    while(a < 4000000 and b < 4000000):
        if(a not in fib):
            fib.append(a)
            if(a % 2 == 0):
                even_fib.append(a)
        if(b not in fib):
            fib.append(b)
            if(b % 2 == 0):
                even_fib.append(b)
        c = a + b
        a = b
        b = c
    print(fib)
    print(even_fib)
    print(sum(even_fib))
    

main()    
    
