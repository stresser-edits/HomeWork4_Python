from itertools import cycle
a = 3
for b in cycle('123'):
    if a > 10:
        break
    print(b)
    a += 1