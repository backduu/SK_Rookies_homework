sentence = input("문장을 입력하세요: ")

# 공백 제거
cleaned_sentence = sentence.replace(" ", "")

# 단어 갯수 get
word_count = len(sentence.split())

print(f"공백 제거: {cleaned_sentence}")
print(f"단어 개수: {word_count}개")