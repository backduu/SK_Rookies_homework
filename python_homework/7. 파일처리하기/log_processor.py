log_lines = [
    "2025-07-20 09:15:00 - WARNING - 메모리 사용량이 높습니다",
    "2025-07-20 10:30:00 - ERROR - 데이터베이스 연결 실패",
    "2025-07-20 11:45:00 - ERROR - 파일을 찾을 수 없음",
    "2025-07-20 12:00:00 - WARNING - 디스크 공간 부족"
]

with open("system.log", "w", encoding="utf-8") as f:
    for line in log_lines:
        f.write(line + "\n")

print("로그 파일이 생성되었습니다.\n")

def filter_logs(level):
    with open("system.log", "r", encoding="utf-8") as f:
        filtered = [line.strip() for line in f if f" - {level} -" in line]
    return filtered

for lvl in ["ERROR", "WARNING"]:
    print(f"{lvl} 레벨 로그들:")
    for entry in filter_logs(lvl):
        print(entry)
    print()