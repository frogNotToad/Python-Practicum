n = int(input())
k = 1
p = 1
while p <= n:
    for i in range(k):
        if p <= n:
            print(p, end=' ')
        p += 1
    k += 1
    print()
