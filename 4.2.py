a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 78, 123, 55]
b = [el for ban, el in enumerate(a) if a[ban - 1] < a[ban]]
print(f'Изначальный список {a}')
del b[0]
print(f'Новый список {b}')