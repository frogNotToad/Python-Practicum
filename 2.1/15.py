h = int(input())
m = int(input())
t = int(input())
h = (h + t // 60) % 24
m = (m + t % 60)
if m >= 60:
    h = (h + 1) % 24
    m %= 60
if len(str(m)) < 2:
    m = '0' + str(m)
if len(str(h)) < 2:
    h = '0' + str(h)
print(f'{h}:{m}')
