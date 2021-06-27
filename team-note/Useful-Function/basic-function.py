# sum()
result = sum([1, 2, 3, 4, 5])
print(result)  # 14

# min(), max()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)  # 2 7

# eval()
result = eval("(3 + 5) * 7")
print(result)  # 56

# sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)  # [1, 4, 5, 8, 9]
print(reverse_result)  # [9, 8, 5, 4, 1]

# sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)  # [('이순신', 75), ('아무개', 50), ('홍길동', 35)]
