def pp(s, w):
    sp = '-' * ((w + 1) * s - 1)

    for i in range(1, s + 1):
        row = '|'.join(f"{i * j:^{w}}" for j in range(1, s + 1))
        print(row)
        if i < s:
            print(sp)


s = int(input())
w = int(input())

pp(s, w)
