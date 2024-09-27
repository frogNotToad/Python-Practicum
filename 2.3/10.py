x, y = 0, 0
s = input()
while s != 'СТОП':
    n = int(input())
    if s == 'СЕВЕР':
        x += n
    if s == 'ВОСТОК':
        y += n
    if s == 'ЮГ':
        x -= n
    if s == 'ЗАПАД':
        y -= n

    s = input()
print(x)
print(y)
