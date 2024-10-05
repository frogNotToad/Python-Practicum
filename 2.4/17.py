k = 0
for _ in range(int(input())):
    s = input()
    if s == s[::-1]:
        k += 1
print(k)
