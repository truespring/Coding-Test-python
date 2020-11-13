from random import *
# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst) # 리스트의 순서를 섞음
# print(lst)
# print(sample(lst, 1)) # 리스트 중에 1개를 무작위로 뽑음

lst = range(1, 21) # 1부터 20까지 숫자를 생성 type은 range
lst = list(lst) # 형변환
shuffle(lst)
winners = sample(lst, 4) # 한 번에 4명을 뽑음
print("-- 당첨자 발표 --")
print(f"치킨 당첨자 : {winners[0]}")
print(f"커피 당첨자 : {winners[1:]}")
print("-- 축하합니다 --")