in_file = open('vocabulary.txt', 'r')

for line in in_file:
    quiz = line.strip().split(": ")
    answ = input("%s: " % (quiz[1]))

    if answ == quiz[0]:
        print("맞았습니다!\n")
    else:
        print("아쉽습니다. 정답은 %s입니다.\n" % (quiz[0]))

in_file.close()