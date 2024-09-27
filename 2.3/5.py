s = 0
n = float(input())
while n != 0:
    s += n
    if n >= 500:
        s -= n * 0.1
    n = float(input())
print(s)
