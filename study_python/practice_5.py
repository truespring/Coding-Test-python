sentence = '나는 석규환입니다.'
print(sentence)
sentence2 = "파이썬을 배우는 중입니다."
print(sentence2)
sentence3 = """
나는 석규환이고,
파이썬을 배우는 중입니다.
"""
print(sentence3)

jumin = "910911-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지
print("월 : " + jumin[2:4]) # 2 부터 4 직전까지
print("일 : " + jumin[4:6]) # 4 부터 6 직전까지

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7 부터 마지막까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지