from itertools import count
from math import factorial
def fact():
    for el in count(1):
        yield factorial(el)
a = fact()
n = int(input('Введите число, факториал которого хотите получить '))
b = 0
for i in a:
    if b < n:
        print(i)
        b += 1
    else:
        break