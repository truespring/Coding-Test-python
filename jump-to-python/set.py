s1 = set([1, 2, 3])
s2 = {1, 2, 3}
print(s1)
print(s2)

l = [1, 2, 2, 3, 3]
newList = list(set(l))

print(newList)

# 순서가 없고 중복을 허용하지 않음
s3 = set('Hello')
print(s3)

s4 = set([1, 2, 3, 4, 5, 6])
s5 = set([4, 5, 6, 7, 8, 9])
print(s4 & s5)  # 교집합
print(s4.intersection(s5))

print(s4 | s5)  # 합집합
print(s4.union(s5))

print(s4 - s5)  # 차집합
print(s4.difference(s5))

s6 = set([1, 2, 3, 4, 5, 6])
s6.add(7)
print(s6)
s6.update([7, 8, 9])
print(s6)
s6.remove(1)
print(s6)
