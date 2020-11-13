# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway = [10, 20, 30]
print(subway)

subway = ["하이", "헬로우", "안녕"]
print(subway.index("헬로우"))

# 리스트에 마지막에 추가
subway.append("니하오")
print(subway)

# 리스트 중간에 삽입
subway.insert(1, "콘니찌와")
print(subway)

# 리스트에서 추출
print(subway.pop()) # 마지막을 뺌
print(subway) # 빼고 난 뒤 변경됨

# 같은 요소를 확인
subway.append("하이")
print(subway)
print(subway.count("하이"))

# 정렬 기능
num_list = [5, 2, 4, 1, 3]
num_list.sort()
print(num_list)

# 순서 뒤집기 기능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형과 함께 사용
num_list = [4, 1, 2, 7, 3]
mix_list = ["Hi", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)