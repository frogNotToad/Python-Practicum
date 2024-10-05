from functools import reduce


def sc(x):
    return reduce(lambda a, b: a + int(b), str(x), 0)


def to(x, base):
    new = ''

    while x > 0:
        r = x % base
        new = str(r) + new
        x = x // base
    return new


n = int(input())
m = sc(to(n, 2))
b = 2
for i in range(3, 11):
    nn = to(n, i)
    if sc(nn) > m:
        m = sc(nn)
        b = i
print(b)
