from functools import reduce


def sc(x):
    return reduce(lambda a, b: a + int(b), str(x), 0)


s = 0
for i in range(int(input())):
    s += sc(int(input()))
print(s)
