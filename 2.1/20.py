n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())

y = n * (m - k1) // (k2 - k1)
x = n - y

print(x, y)
