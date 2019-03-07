from random import randint

vocab = {}

in_file = open('vocabulary.txt', 'r')

for line in in_file:
    quiz = line.strip().split(": ")
    vocab[quiz[1]] = quiz[0]

print(vocab)

keys = list(vocab.keys())

while True:
    index = randint(0, len(keys) - 1)
    korean_word = keys[index]
    english_word = vocab[korean_word]

    answ = input("%s: " % (korean_word))

    # 코드를 입력하세요.
    if answ == english_word:
        print("맞았습니다!\n")
    else:
        print("틀렸습니다. 정답은 %s입니다.\n" % (english_word))

in_file.close()
