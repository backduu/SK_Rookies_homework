numbers = list(range(1, 11))
squares = list(map(lambda x: x**2, numbers))
over_five = list(filter(lambda x: x > 5, numbers))
over_five_squares = list(map(lambda x: x**2, over_five))

print(f"원본 숫자: {numbers}")
print(f"모든 수의 제곱: {squares}")
print(f"5보다 큰 수들: {over_five}")
print(f"5보다 큰 수들의 제곱: {over_five_squares}")
