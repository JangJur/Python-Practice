for a in range(1, 332):
    for b in range(a + 1, 500):
        c = 1000 - a - b
        # 코드를 작성하세요.
        if a * a + b * b == c * c and a < b < c:
            print(a * b * c)