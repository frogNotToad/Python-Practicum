n = int(input())
m = 0
for digit in str(n):
    m = max(m, int(digit))
print(m)
