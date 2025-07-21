fruits = ['사과', '바나나', '오렌지', '포도', '딸기']

print(f"과일 목록: {fruits}")

findOne = input("찾을 과일을 입력하세요: ")

if findOne in fruits:
    print(f"'{findOne}'가 목록에 있습니다!")
else:
    print(f"'{findOne}'는 목록에 없습니다.")