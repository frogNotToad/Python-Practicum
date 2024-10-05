n = int(input())

a = []
for i in range(n):
    a.append([0] * n)

for i in range(n):
    for j in range(n):
        a[i][j] = min(i + 1, j + 1, n - i, n - j)

m = len(str(n // 2 if n % 2 == 0 else n // 2 + 1))
for i in range(n):
    for j in range(n):
        print(f'{a[i][j]:{m}}', end=' ')
    print()
