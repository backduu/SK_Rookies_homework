nums1 = [2, 4, 6, 8, 10]
nums2 = [1, 3, 5, 7, 12]

print(f"숫자 리스트 {nums1}")
print("모든 수가 짝수인가?", all(n % 2 == 0 for n in nums1))
print("하나라도 10보다 큰 수가 있는가?", any(n > 10 for n in nums1))

print(f"\n숫자 리스트2: {nums2}")
print("모든 수가 짝수인가?", all(n % 2 == 0 for n in nums2))
print("하나라도 10보다 큰 수가 있는가?", any(n > 10 for n in nums2))
