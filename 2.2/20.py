a = input()
b = input()
c = input()

s = []
if 'зайка' in a:
    s.append(a)
if 'зайка' in b:
    s.append(b)
if 'зайка' in c:
    s.append(c)
s.sort()
print(s[0], len(s[0]))
