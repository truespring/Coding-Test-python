# 사전
cabinet = {3:"석규환", 100:"김창용"} # 키:벨류의 형태
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # error 발생 -> 그 다음 부분은 실행하지 않음
print(cabinet.get(5)) # 값이 없을때 none 을 출력하고 다음으로 넘어감
print(cabinet.get(5, "사용 가능")) # 해당 값이 none 일 때 삽입가능
print(3 in cabinet) # boolean type : True
print(5 in cabinet) # boolean type : False

cabinet = {"A-3":"석규환", "B-100":"김창용"}
print(cabinet["A-3"])

# 새로운 값
print(cabinet)
cabinet["A-3"] = "박덕규" # 있으면 값이 바뀜
cabinet["C-20"] = "윤재웅" # 값이 없으면 추가
print(cabinet)

# 값 제거
del cabinet["A-3"]
print(cabinet)

# 키들만 출력
print(cabinet.keys())

# 밸류만 출력
print(cabinet.values())

# 키 밸류 출력
print(cabinet.items())

# 모두 제거
cabinet.clear()
print(cabinet)