array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]


def my_key(x):
    return x[1]


print(sorted(array, key=my_key))  # [('이순신', 32), ('홍길동', 50), ('아무개', 74)]
print(sorted(array, key=lambda x: x[1]))  # [('이순신', 32), ('홍길동', 50), ('아무개', 74)]
