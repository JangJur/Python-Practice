p_year = 1988
r_year = 2016
b_money = 50000000
a_money = 1100000000
rate = 0.12
i = 1

while i <= (r_year - p_year):
    b_money *= (1 + rate)
    i += 1

if b_money > a_money:
    print("%d원 차이로 동일 아저씨의 말씀이 맞습니다." % (b_money - a_money))
elif b_money < a_money:
    print("%d원 차이로 미란 아주머니의 말씀이 맞습니다." % (a_money - b_money))
else:
    print("두분 다 말씀이 맞습니다.")