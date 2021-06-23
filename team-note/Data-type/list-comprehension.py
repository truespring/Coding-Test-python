# 0부터 9까지의 수를 포함하는 리스트
array = [i for i in range(10)]

print(array)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

print(array)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i * i for i in range(10)]

print(array)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 코드 1: 리스트 컴프리헨션
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

print(array)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 코드 2: 일반적인 코드
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)

print(array)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# N X M 크기의 2차원 리스트 초기화(좋은 예시)
n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

array[1][1] = 5
print(array)  # [[0, 0, 0], [0, 5, 0], [0, 0, 0], [0, 0, 0]]

# N X M 크기의 2차원 리스트 초기화(잘못된 예시)
n = 4
m = 3
array = [[0] * m] * n
print(array)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

array[1][1] = 5
print(array)  # [[0, 5, 0], [0, 5, 0], [0, 5, 0], [0, 5, 0]]
