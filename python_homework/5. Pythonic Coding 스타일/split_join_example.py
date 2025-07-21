text = "Python is awesome programming language"
words = text.split()
joined_hyphen = "-".join(words)
joined_upper = " ".join(word.upper() for word in words)
print(f"원본 문자열: {text}")
print(f"분리된 단어들: {words}")
print(f"하이픈으로 연결: {joined_hyphen}")
print(f"대문자로 변환 후 공백으로 연결: {joined_upper}")