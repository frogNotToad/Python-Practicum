s = input()
a = [int(s[0]), int(s[1]), int(s[2])]
a.sort()
print('YES' if a[0] + a[2] == a[1] * 2 else 'NO')
