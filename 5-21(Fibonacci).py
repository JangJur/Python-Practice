pre = 0
cur = 1
temp = 0
cnt = 20
i = 0

while i < cnt:
    print(cur)
    temp = pre
    pre = cur
    cur += temp

    i += 1
