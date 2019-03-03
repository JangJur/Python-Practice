PI = 3.14       # 원주율

def calculate_area(r):
    return PI * r * r

radius = 6     #반지름
print("반지름이 %f면 원 넓이는 % f" % (radius, calculate_area(radius)))

PI = 0
radius = 12     #반지름
print("반지름이 %f면 원 넓이는 % f" % (radius, calculate_area(radius)))
