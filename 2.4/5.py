k = 0
for n in range(int(input())):
    a = []
    s = input()
    while s != 'ВСЁ':
        a.append(s)
        s = input()
    if 'зайка' in a:
        k += 1
print(k)
