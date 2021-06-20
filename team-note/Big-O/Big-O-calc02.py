# 시간 복잡도 계산해보기

array = [3, 5, 1, 2, 4]  # 5개의 데이터(N = 5)

for i in array:
    for j in array:
        temp = i * j
        print(temp)

# 시간 복잡도: O(N<sup>2</sup>)
# 참고로 모든 2중 반복문의 시간 복잡도가 O(N<sup>2</sup>)인 것은 아닙니다.
# 소스코드가 내부적으로 다른 함수를 호출한다면 그 함수의 시간 복잡도까지 고려해야 합니다.
