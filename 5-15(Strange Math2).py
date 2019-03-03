i = 1;
sum = 0;

while i < 1000:
    if (i % 2 == 0):
        sum += i
    elif (i % 3 == 0):
        sum += i
    i += 1

print(sum)