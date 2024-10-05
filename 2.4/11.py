def isp(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


k = 0
for _ in range(int(input())):
    if isp(int(input())):
        k += 1
print(k)
