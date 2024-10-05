a = int(input())
b = int(input())
m = len(str(a * b))
aa = []
for _ in range(a):
    aa.append([0] * b)

for i in range(b):
    for j in range(1, a + 1):
        aa[j - 1][i] = j + a * i

for i in range(a):
    for j in range(b):
        print(f'{aa[i][j]:{m}}', end=' ')
    print()
