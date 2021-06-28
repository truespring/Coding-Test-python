n = int(input())

for i in range(n):
    num = 0
    sum = 0
    avg = 0

    data = list(map(int, input().split()))
    for j in range(0, data[0]):
        sum += data[j+1]
        if j == data[0] - 1:
            avg = sum / data[0]

    for j in range(0, data[0]):
        if avg < data[j+1]:
            num += 1
    temp = float(round(num / data[0] * 100, 3))
    print('{:.3f}%'.format(temp))
