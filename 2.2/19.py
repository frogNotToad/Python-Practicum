x = float(input())
y = float(input())

if x ** 2 + y ** 2 > 100:
    print('Вы вышли в море и рискуете быть съеденным акулой!')
else:
    ok = True
    if y >= 0:
        if x >= 0:
            if x ** 2 + y ** 2 <= 25:
                ok = False
        else:
            if x >= -4:
                if y <= 5:
                    ok = False
            else:
                if y < x * 5 / 3:
                    ok = False
    else:
        if y >= 0.25 * x ** 2 + 0.5 * x - 35 / 4:
            ok = False
    if ok:
        print('Зона безопасна. Продолжайте работу.')
    else:
        print('Опасность! Покиньте зону как можно скорее!')
