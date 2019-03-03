def calculate_change(payment, cost):
    # 코드를 작성하세요.
    exchange_moneny = payment - cost

    fifty_count = int(exchange_moneny / 50000)
    ten_count = int(exchange_moneny % 50000 / 10000)
    five_count = int(exchange_moneny % 10000 / 5000)
    one_count = int(exchange_moneny % 5000 / 1000)

    print("50000원 지폐: %d장"% (fifty_count))
    print("10000원 지폐: %d장" % (ten_count))
    print("5000원 지폐: %d장" % (five_count))
    print("1000원 지폐: %d장" % (one_count))
# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
