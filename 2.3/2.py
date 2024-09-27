n = 0
s = input()
while s != 'Приехали!':
    n += 1 if 'зайка' in s else 0
    s = input()
print(n)
