list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

merged = sorted(set(list1 + list2))
common = sorted(set(list1).intersection(list2))

print(f"리스트1: {list1}")
print(f"리스트2: {list2}")
print(f"병합된 리스트: {merged}")
print(f"공통 요소: {common}")
