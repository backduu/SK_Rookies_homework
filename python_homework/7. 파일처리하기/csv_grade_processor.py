import csv

grades = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 78,
    "최수진": 95
}

with open("grades.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["이름", "점수"])
    for name, score in grades.items():
        writer.writerow([name, score])

print("학생 성적이 grades.csv에 저장되었습니다.\n")
print("성적 분석 결과:")

total = 0
count = 0

with open("grades.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # 헤더 건너뛰기
    for row in reader:
        name, score = row[0], int(row[1])
        print(f"{name}: {score}점")
        total += score
        count += 1

average = total / count
print(f"전체 평균: {average:.1f}점")
