def is_palindrome(word):
    # 코드를 입력하세요.
    word = list(word)
    t_d = 0
    for i in range(int(len(word) / 2)):
        if word[i] != word[len(word) - i - 1]:
            t_d += 1

    if t_d >= 1:
        return False
    else:
        return True

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
