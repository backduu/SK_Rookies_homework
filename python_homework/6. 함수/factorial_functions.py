def factorial_recursive(n):
    return 1 if n == 0 else n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

for n in [5, 7]:
    print(f"{n}! (재귀) = {factorial_recursive(n)}")
    print(f"{n}! (반복) = {factorial_iterative(n)}")