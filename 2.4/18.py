from functools import reduce

n = int(input())
a = []
p = 1
k = 1
while p <= n:
    aa = []
    for i in range(k):
        if p <= n:
            aa.append(p)
        p += 1
    k += 1
    a.append(aa)

mw = reduce(lambda a, b: a + len(str(b)), a[-1], 0) + len(a[-1]) - 1
for e in a:
    ll = reduce(lambda x, y: x + len(str(y)), e, 0) + len(e) - 1
    fh = (mw - ll) // 2
    print(" " * fh, " ".join(map(str, e)), " " * (mw - ll - fh), sep='')
