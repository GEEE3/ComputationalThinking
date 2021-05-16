# by GEEE3, May 12, 2021
# 다음과 같이 학생의 성적을 출력하시오
# 1. 학생의 점수는 다음과 같다 score = [82, 98, 100, 40, 75, 55, 73, 24, 10, 64]
# 2. 90점 이상은 A, 70점까지는 B, 50점 까지는 C, 나머지는 F를 주는 프로그램을 작성하시오
score = [82, 98, 100, 40, 75, 55, 73, 24, 10, 64]
student = 0

for num in score:
    student += 1
    if num >= 90:
        print("{}번 학생의 성적은 A입니다." .format(student))
    elif num >= 70:
        print("{}번 학생의 성적은 B입니다." .format(student))
    elif num >= 50:
        print("{}번 학생의 성적은 C입니다." .format(student))
    else:
        print("{}번 학생의 성적은 F입니다." .format(student))