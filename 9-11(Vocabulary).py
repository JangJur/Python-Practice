out_file = open('vocabulary.txt', 'w')


while True:
    voca = input("영어 단어를 입력하세요: ")
    if voca == 'q':
        break
    mean = input("한국어 뜻을 입력하세요: ")

    out_file.write("%s: %s\n" % (voca, mean))

out_file.close()

in_file = open('vocabulary.txt', 'r')

for line in in_file:
    print(line.strip())

in_file.close()
