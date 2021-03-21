# by GEEE3, March 19, 2021
# 세 개의 수를 입력 받아 그 합과 평균을 출력하는 script 작성할 것
# (평균은 소수점 한자리까지 출력)
num = input("정수 숫자 3개를 입력 : ")
first, second, third = num.split()
first = int(first)
second = int(second)
third = int(third)

print("입력 받은 값 :", first, second, third)
print("총합 : {}" .format(first + second + third))
print("평균 : {:.1f}" .format((first + second + third) / 3))