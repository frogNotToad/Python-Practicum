from functools import reduce


def sc(x):
    return reduce(lambda a, b: a + int(b), str(x), 0)


p = ''
s = 0
for _ in range(int(input())):
    name = input()
    n = int(input())
    if sc(n) >= s:
        s = sc(n)
        p = name
print(p)
