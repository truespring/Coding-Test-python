from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0 ~ 10.0 미만
print(int(random() * 10)) # 0 ~ 10
print(int(random() * 10)) # 0 ~ 10
print(int(random() * 10)) # 0 ~ 10
print(int(random() * 10) + 1) # 0 ~ 10 이하

print(randrange(1, 45)) # 1 ~ 45 미만의 임의의 값 생성

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성