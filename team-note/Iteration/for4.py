# 학생들의 합격 여부 판단 예제
# 2) 특정 번호의 학생은 제외하기

score = [90, 85, 77, 65, 97]
cheating_student_list = {2, 4}

for i in range(5):
    if i + 1 in cheating_student_list:
        continue
    if score[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

# 1 번 학생은 합격입니다.
# 5 번 학생은 합격입니다.
