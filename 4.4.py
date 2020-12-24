from itertools import groupby
a = [2, 2, 7, 23, 1, 44, 44, 3, 10, 7, 4, 11]
b = [el for el, _ in groupby(a)]
print(b)

