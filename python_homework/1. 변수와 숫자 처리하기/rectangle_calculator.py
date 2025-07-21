#가로와 세로 입력
width = int(input("가로 길이를 입력하세요: "))
height = int(input("세로 길이를 입력하세요: "))

# 계산식
area = width * height
perimeter = 2 * (width + height)

print(f"직사각형의 넓이: {area}")
print(f"직사각형의 둘레: {perimeter}")
