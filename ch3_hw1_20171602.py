# by GEEE3, March 10, 2021
# 어느 학생의 과제 점수가 21.9, 37, 13.6일 때, 학생의 평균 과제 점수를 구하는 script 작성 할 것
import math

# 1. 각 점수는 변수에 저장할 것
subject1 = 21.9
subject2 = 37
subject3 = 13.6
average = (subject1 + subject2 + subject3) / 3

# 2. 평균 값의 소수점 이하는 버리고 출력할 것
# 3. math 모듈의 함수를 사용할 것
print("average :", math.trunc(average))