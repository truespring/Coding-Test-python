# Map, Json, Object, Hash

dic = {'name': 'Eric', 'age': 13}

print(dic['name'])

a = {1: 'a'}
del a[1]
a['name'] = "sksk"

print(a)
print(dic.keys())
print(dic.values())
print(dic.items())

for k in dic:
    print(k)

for v in dic.values():
    print(v)

for k, v in dic.items():
    print("키는 : " + str(k))
    print("벨류는 : " + str(v))

b = {1: 'a', 2: 'b', 3: 'c'}

print(b.get(4, '없음'))
print(4 in b)
