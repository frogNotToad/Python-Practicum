def guess_number():
    left = 1
    right = 1000

    while True:
        m = (left + right) // 2
        print(m)
        response = input()

        if response == "Угадал!":
            return
        elif response == "Больше":
            left = m + 1
        elif response == "Меньше":
            right = m - 1


guess_number()
