in_file = open('chicken.txt', 'r', encoding='UTF-8')

sum = 0
cnt = 0

for line in in_file:
    data = line.strip().split()
    sum += int(data[1])
    cnt += 1

average = sum / cnt

print(average)

in_file.close()
