numbers = [1,2,3,4,5,6,7,8,9,10]
evens = [n for n in numbers if n % 2 == 0]
squares = [n**2 for n in evens]

print(f"원본 리스트: {numbers}")
print(f"짝수들: {evens}")
print(f"짝수의 제곱: {squares}")
