a = []
n = int(input())
for i in range(1, n - 1):
    for j in range(1, n - i):
        a.append((i, j, n - i - j))
a.sort()
print('А Б В')
for e in a:
    print(*e)
