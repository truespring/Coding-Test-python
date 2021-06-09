a = True
print(a)
print(type(a))

# 값이 있는 문자열 True
# 값이 없는 문자열 "" False
# 값이 있는 리스트 True
# 값이 없는 리스트 [] False
# 값이 없는 튜플, 딕셔너리 (), {} False
# 1 True, 0 False, None False

if a:
    print(a)

b = "안녕"
if b:
    print(b)

c = ""
if c:
    print(c)

d = [1, 2, 3, 4]
while d:
    d.pop()
    print(d)
