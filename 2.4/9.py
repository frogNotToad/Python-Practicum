from functools import reduce


def mn(x: int) -> int:
    return reduce(lambda a, b: max(a, int(b)), str(x), 0)


for _ in range(int(input())):
    n = int(input())
    print(mn(n), end='')
