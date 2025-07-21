input1 = int(input("첫 번째 숫자를 입력하세요: "))
input2 = int(input("두 번째 숫자를 입력해주세요: "))

print(f"{input1} + {input2} = {input1 + input2}")
print(f"{input1} - {input2} = {input1 - input2}")
print(f"{input1} * {input2} = {input1 * input2}")
if input2 != 0 :
    print(f"{input1} / {input2} = {input1 / input2}")
else :
    print(f"[ZeroDivisionError] 0으로 나눌 수 없습니다.")