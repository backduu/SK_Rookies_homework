score = 85
result = "합격" if score >= 60 else "불합격"
print(f"점수: {score}, 결과: {result}")

age = 17
status = "미성년자" if age < 18 else "성인"
print(f"나이: {age}, 상태: {status}")

nums = [42, 15, 3, 8]
max_val = max(nums)
print(f"숫자들의 최대값: {max_val}")

positives = [n for n in nums if n > 0]
print(f"양수들: {positives}")