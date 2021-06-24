# 데이터의 개수 입력
n = int(input())  # 5
# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))  # 65 90 75 34 99

data.sort(reverse=True)
print(data)  # [99, 90, 75, 65, 34]

# 무조건 데이터가 정해진 개수로만 들어오는 경우
a, b, c = map(int, input().split())  # 1 3 4

print(a, b, c)  # 1 3 4