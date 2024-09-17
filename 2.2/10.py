s = input()
a = [int(s[-1]) + int(s[-2]), int(s[0]) + int(s[1])]
print(max(a), min(a), sep='')
