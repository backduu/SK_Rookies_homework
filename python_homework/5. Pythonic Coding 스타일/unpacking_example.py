coord = (10, 20)
x, y = coord
print(f"좌표: x={x}, y={y}")

a, b, c = [1, 2, 3]
print(f"리스트 언패킹: a={a}, b={b}, c={c}")

def total(*args):
    return sum(args)
print(f"가변 인수의 합: {total(10, 20, 30)}")

def print_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}={v}", end=", ")

print("키워드 인수들:", end=" ")
print_info(name="김철수", age=25, city="서울")
