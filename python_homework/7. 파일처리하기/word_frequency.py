from collections import Counter

text = """파이썬 프로그래밍은 쉬운 언어입니다.
파이썬은 배우기 쉽고 강력한 언어입니다.
프로그래밍 언어 중 파이썬은 많은 사람들이 사용합니다."""

words = text.replace('\n', ' ').split()

freq = Counter(words)

print("단어 빈도 분석 결과:")
for word, count in freq.items():
    print(f"{word}: {count}번")