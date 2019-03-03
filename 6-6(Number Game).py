from random import randint
i = 4
ran = randint(1, 20)

while i > 0:
    num = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % (i)))
    if num < ran:
        print("Up")
    elif num > ran:
        print("Down")
    else:
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (i))
        break
    i -= 1

if i == 0:
    print("아쉽습니다. 정답은 %d였습니다." %(ran))
