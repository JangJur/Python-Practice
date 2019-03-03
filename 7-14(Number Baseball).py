from random import randint

cnt = 0
num = []

while True:

    answ_num = []
    strike = 0
    ball = 0

    while len(num) < 3:
        random_num = randint(0, 9)

        while random_num in num:
            random_num = randint(0, 9)
        num.append(random_num)

    print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
    print()

    print("세 수를 하나씩 차례대로 입력하세요.")

    i = 0
    while i < len(num):
        check_num = int(input("%d번째 수를 입력하세요: " % (i + 1)))
        if check_num in answ_num:
            print("중복되는 수 입니다. 다시 입력해주세요.")
            continue
        elif check_num > 9 or check_num < 0:
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
            continue

        answ_num.append(check_num)
        if answ_num[i] == num[i]:
            strike += 1
        elif answ_num[i] in num:
            ball += 1
        i += 1

    print("%dS %dB" % (strike, ball))

    cnt += 1

    if strike == 3:
        print("축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (cnt))
        break
