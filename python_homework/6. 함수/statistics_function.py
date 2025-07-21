import statistics

def get_stats(data):
    avg = statistics.mean(data)
    maximum = max(data)
    minimum = min(data)
    stddev = statistics.stdev(data)
    return avg, maximum, minimum, stddev

nums = [10, 20, 30, 40, 50]
avg, max_val, min_val, stddev = get_stats(nums)

print(f"숫자들: {nums}")
print(f"평균: {avg:.1f}")
print(f"최댓값: {max_val}")
print(f"최솟값: {min_val}")
print(f"표준편차: {stddev:.2f}")