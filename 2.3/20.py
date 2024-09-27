def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    h = 0
    for i in range(n):
        b = a[i]
        h_n = b % 256
        r_n = b // 256 % 256
        m_n = b // 256 // 256

        if h_n >= 100:
            print(i)
            return

        e_h_n = (37 * (m_n + r_n + h)) % 256
        if e_h_n != h_n:
            print(i)
            return

        h = h_n
    print(-1)


if __name__ == '__main__':
    main()
