# 세트 (set)
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set) # {1, 2, 3}

java = {"석규환", "정혜선", "김도빈"}
python = set(["최은실", "석규환"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("정혜선")
print(python)

# java 를 까먹음
java.remove("김도빈")
print(java)