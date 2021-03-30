# by GEEE3, March 24, 2021
# 세 개의 정수를 입력 받아 내림차순으로 정렬하여 출력하는 script 작성하라
# (한개의 입력 함수만 사용 할 것)
num = input("세 개의 정수를 입력하시오 : ")
first, second, third = num.split()
first = int(first)
second = int(second)
third = int(third)

if second < third:
    second, third = third, second
if first < second:
    if first < third:
        first, third = third, first
        first, second = second, first
    else:
        first, second = second, first

print("내림차순 정렬 :", first, second, third)