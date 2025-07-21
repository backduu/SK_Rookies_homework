squares = {n: n**2 for n in range(1, 6)}
even_squares = {n: n**2 for n in range(1, 11) if n%2 == 0}

print(f"1부터 5까지의 제곱 딕셔너리: {squares}")
print(f"짝수만의 제곱 딕셔너리: {even_squares}")
