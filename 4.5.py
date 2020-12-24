from functools import reduce
i = range(100, 1001, 2)
a = reduce(lambda x,y: x * y, i)

print(f'Произведение всех чисел от 100 до 1000 кратных 2-ум = {a}')