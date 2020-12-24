def sallary():
    try:
        a = int(input('Введите выработку в часах '))
        b = int(input('Введите ставку в час '))
        c = int(input('Введите сумму премии '))
        d = a * b + c
        print(f'Заработная плата {d}')
    except ValueError:
        return print('Перезапустите программу и введите числo')
sallary()