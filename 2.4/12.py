a = int(input())
b = int(input())
sh = [0] * b
aa = []
for i in range(a):
    arr = []
    for j in range(1, b + 1):
        arr.append(j + b * i)
        if len(str(arr[-1])) > sh[j - 1]:
            sh[j - 1] = len(str(arr[-1]))
    aa.append(arr)

for i in range(a):
    for j in range(b):
        print(f'{aa[i][j]:{sh[j]}}', end=' ')
    print()
