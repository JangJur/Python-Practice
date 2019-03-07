# 정수 n부터 1까지 츨략
def countdown(n):
    if n > 0:
        print(n)
        countdown(n-1)

countdown(4)

def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n

print(factorial(4))
