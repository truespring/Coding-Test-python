data = {
    '사과': 'Apple',
    '바나나': 'Banana',
    '코코넛': 'Coconut'
}

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트ㅡ
value_list = data.values()
print(key_list)  # dict_keys(['사과', '바나나', '코코너'])
print(list(key_list))  # ['사과', '바나나', '코코넛']
print(value_list)  # dict_values(['Apple', 'Banana', 'Coconut'])
print(list(value_list))  # ['Apple', 'Banana', 'Coconut']

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])
# Apple
# Banana
# Coconut
