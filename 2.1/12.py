a = input()
b = input()
m = max(len(a), len(b))
a = '0' * max(0, m - len(a)) + a
b = '0' * max(0, m - len(b)) + b
for i in range(m):
    print(str(int(a[i]) + int(b[i]))[-1], end='')
