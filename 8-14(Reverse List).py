numbers = [2, 4, 6, 8, 10, 12, 14]

# 리스트 뒤집기
# 코드를 입력하세요.
for index in range(int(len(numbers) / 2)):
    temp = numbers[index]
    numbers[index] = numbers[len(numbers) - index - 1]
    numbers[len(numbers) - index - 1] = temp

print("뒤집어진 리스트: " + str(numbers))