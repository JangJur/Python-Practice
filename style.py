PI = 3.14       # 원주율

# 반지름이 r인 원의 둘레 계산
def calculate_circumference(r):
    return 2 * PI * r

# 반지름이 r인 원의 넓이 계산
def calculate_area(r):
    return PI * r * r

#반지름이 4인 구의 부피 계산
def calculate_volume(r):
    return 4 / 3 * PI * r * r *r

# 반지름이 4인 경우
radius = 4      # 반지름
print(calculate_circumference(radius))
print(calculate_area(radius))
print(calculate_volume(radius))

# 반지름이 8인 경우
radius = 8      # 반지름
print(calculate_circumference(radius))
print(calculate_area(radius))
print(calculate_volume(radius))
