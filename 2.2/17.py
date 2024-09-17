from math import sqrt

a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b == 0:
        if c == 0:
            print("Infinite solutions")
        else:
            print("No solution")
    else:
        x = -c / b
        print(f"{x:.2f}")
else:
    D = b ** 2 - 4 * a * c
    if D < 0:
        print("No solution")
    elif D == 0:
        x = -b / (2 * a)
        print(f"{x:.2f}")
    else:
        x1 = (-b - sqrt(D)) / (2 * a)
        x2 = (-b + sqrt(D)) / (2 * a)
        result = sorted([x1, x2])
        print(f"{result[0]:.2f} {result[1]:.2f}")
