#!C:\Python34\python.exe
def MultipleOf3or5(num):
    if(num % 3 == 0 or num % 5 == 0):
        return True
    else:
        return False
    
def main_loop():
    multiples = []
    for x in range(1000):
        if(MultipleOf3or5(x)):
            multiples.append(x)
    print(sum(multiples))
    
def main_comprehension():
    multiples = 0
    multiples = [x for x in range(1000) if MultipleOf3or5(x)]
    print(sum(multiples))

#233168
main_comprehension()
