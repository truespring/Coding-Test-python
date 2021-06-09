from copy import copy

a = [1, 2, 3]
b = a
a[1] = 4
print(a)
print(b)
print(id(a))
print(id(b))
print(a is b)  # 같은 주소값을 가리키고 있는지 확인

b = a[:]  # 슬라이싱하여 값을 전달(새로운 객체 생성)
a[1] = 2
print(a)
print(b)
print(id(a))
print(id(b))
print(a is b)

a = [1, 2, 3]
b = copy(a)
a[1] = 4
print(id(a))
print(id(b))

c, d = ('python', 'life')
print(c)
print(d)
(c, d) = ('python', 'life')
print(c)
print(d)
(c, d) = 'python', 'life'
print(c)
print(d)
[c, d] = ['python', 'life']
print(c)
print(d)
c = d = 'hello'
print(c)
print(d)

a = 3
b = 5
a, b = b, a
print(a)  # 5
print(b)  # 3
