import datetime
import random

now = datetime.datetime.now()
print(f"현재 날짜와 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")

weekday = now.strftime('%A')  # 영어 요일
weekday_korean = {
    "Monday": "월요일",
    "Tuesday": "화요일",
    "Wednesday": "수요일",
    "Thursday": "목요일",
    "Friday": "금요일",
    "Saturday": "토요일",
    "Sunday": "일요일"
}[weekday]

print(f"포맷된 날짜: {now.year}년 {now.month:02d}월 {now.day:02d}일 {weekday_korean}")

random_int = random.randint(1, 10)
print(f"임의의 숫자: {random_int}")

random_float = round(random.uniform(1.0, 10.0), 2)
print(f"임의의 실수: {random_float}")

fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
chosen = random.choice(fruits)
print(f"임의의 리스트 요소: {chosen}")

shuffled = fruits.copy()
random.shuffle(shuffled)
print(f"섞인 리스트: {shuffled}")