a = int(input())
b = int(input())
print(*[i for i in range(a, b + (-1 if b < a else 1), -1 if b < a else 1)])
