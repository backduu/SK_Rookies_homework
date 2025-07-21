from math_operations import circle_area, rectangle_area, factorial, gcd

# 원의 넓이 계산
circle = circle_area(5)
print(f"원의 넓이: {circle}")

# 직사각형 넓이 계산
rectangle = rectangle_area(10, 5)
print(f"직사각형 넓이: {rectangle}")

# 팩토리얼 계산
fact = factorial(5)
print(f"팩토리얼 5! = {fact}")

# 최대공약수 계산
common_divisor = gcd(48, 18)
print(f"최대공약수(48, 18) = {common_divisor}")