import time

#with comprehensions
def main():
    print(max(x*y for x in range(100,1000) for y in range(100,1000) if str(x*y) == str(x*y)[::-1]))

#without comprehensions
def main2():
    pal = []
    for a in range(100,1000):
        for b in range(100,1000):
            if str(a*b)[::-1] == str(a*b):
                pal.append(a*b)
    print(max(pal))
    

main()
main2()