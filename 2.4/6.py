from math import gcd
from functools import reduce

a = [int(input()) for _ in range(int(input()))]
print(reduce(gcd, a))
