#перевірка, чи є число простим
from math import sqrt

def square(x):
    return x**2

def simple(x):
    if x == 0:
        return False
    if x in [1,2,3]:
        return True
    else:
        lime = round(sqrt(x)+1)
        for i in range(2,lime):
            if x % i != 0:
                f = True
            else:
                return False
                break
        if f:
            return True
mas = []
for i in range(51):
    if simple(i):
        mas.append(i)
a = list(map(square, mas))
#коротше без map таким чином:
#a = [square(x) for x in range(51) if simple(x) ]
print(a)