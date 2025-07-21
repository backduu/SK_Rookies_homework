lines = [
    "안녕하세요",
    "파이썬 파일 처리를 연습하고 있습니다",
    "오늘은 좋은 날씨입니다"
]

with open("testBackduu.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")

f.close()