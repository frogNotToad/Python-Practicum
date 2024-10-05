def s(x, y):
    m = [[0] * y for _ in range(x)]

    num = 1
    for i in range(x):
        if i % 2 == 0:
            for j in range(y):
                m[i][j] = num
                num += 1
        else:
            for j in range(y - 1, -1, -1):
                m[i][j] = num
                num += 1

    return m


a = int(input())
b = int(input())
m = len(str(a * b))

aa = s(a, b)
for i in range(a):
    for j in range(b):
        print(f'{aa[i][j]:{m}}', end=' ')
    print()
