numbers = [15, 3, 27, 8, 19, 12, 31]

max_num = max(numbers)
min_num = min(numbers)
sorted_nums = sorted(numbers, reverse=True)
second_max = sorted_nums[1]

print(f"숫자 목록: {numbers}")
print(f"최댓값: {max_num}")
print(f"최솟값: {min_num}")
print(f"두 번째로 큰 값: {second_max}")
