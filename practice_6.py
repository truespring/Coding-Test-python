python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # 인덱스에 해당하는 문자가 대문자인지 확인
print(len(python)) # 해당 문자열의 길이를 출력
print(python.replace("Python", "Java")) # 해당 문자열에서 입력한 문자열을 찾아 바꿈

index = python.index("n") # 해당 문자가 몇 번째 index인지 찾음
print(index)
index = python.index("n", index + 1) # 해당 문자의 두 번째 index를 찾음
print(index)

print(python.find("n"))
print(python.find("Java")) # 해당 문자열이 없다면 -1을 출력
# print(python.index("Java")) # 해당 문자열이 없다면 에러를 띄우고 프로그램 종료

print(python.count("n")) # 해당 문자가 몇 번 존재하는지 찾음