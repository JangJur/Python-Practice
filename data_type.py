# -*- coding:utf-8 -*-
# 형 변환 (Type Conversion / Type Casting)

# 숫자형 => 숫자형
print(int(3.8))     # int = > integer (정수)
print(float(3))     # float => floating point(소수)

# 문자열 => 숫자형
print(int("2") + int("5"))      # print(2 + 5)
print(float("1.1") + float("2.5"))      #printf(1.1 + 2.5)

# 숫자형 => 문자열
# str => string (문자열)
print(str(2) + str(5))      # print("2" + "5")
print("제 나이는 " + str(7)+ "살입니다.")

# 주의!!
print(int("Hello world!"))
