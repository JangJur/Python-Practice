in_file = open('chicken.txt', 'r', encoding='UTF-8')

for line in in_file:
    print(line.strip())

in_file.close()
