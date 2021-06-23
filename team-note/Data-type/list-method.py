# 리스트 관련 기타 메서드
a = [1, 4, 3]
print("기본 리스트: ", a)  # [1, 4, 3]

# 리스트에 원소 삽입
a.append(2)
print("삽입: ", a)  # [1, 4, 3, 2]

# 오름차순 정렬
a.sort()
print("오름차순 정렬: ", a)  # [1, 2, 3, 4]

# 내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬: ", a)  # [4, 3, 2, 1]

a = [4, 3, 2, 1]

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ", a)  # [1, 2, 3, 4]

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에3 추가: ", a)  # [1, 2, 3, 3, 4]

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))  # 2

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)  # [2, 3, 3, 4]

# 리스트에서 특정 값을 가지는 원소를 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}  # 집합 자료형

# remove_list 에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)  # [1, 2, 4]
