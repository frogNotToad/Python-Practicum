a = input()
b = input()

s = list(sorted([a[0], a[1], b[0], b[1]]))
print(s[3] + str((int(s[1]) + int(s[2])) % 10) + s[0])
