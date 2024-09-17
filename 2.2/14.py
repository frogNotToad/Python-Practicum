s = input()
a = list(sorted([s[0], s[1], s[2]]))
if a[0] != '0':
    print(a[0] + a[1], a[2] + a[1])
elif a[1] != '0':
    print(a[1] + a[0], a[2] + a[1])
else:
    print(a[2] + a[1], a[2] + a[1])
