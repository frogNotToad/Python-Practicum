a = int(input())
b = int(input())
c = int(input())

s = [a, b, c]
s.sort()
if s[2] ** 2 == s[1] ** 2 + s[0] ** 2:
    print('100%')
elif s[2] ** 2 > s[1] ** 2 + s[0] ** 2:
    print('велика')
else:
    print('крайне мала')
