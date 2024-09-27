def prime_factors(num):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num //= 2

    for i in range(3, int(num ** 0.5) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num //= i

    if num > 2:
        factors.append(num)

    return factors


n = int(input())
r = prime_factors(n)

print(" * ".join(map(str, r)))
