total = 0

while True:
    number = int(input("숫자를 입력하세요 (0을 입력하면 종료): "))
    if number == 0:
        break
    total += number

print(f"입력된 숫자들의 합: {total}")
