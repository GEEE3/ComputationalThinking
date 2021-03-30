# by GEEE3, March 24, 2021
# 십의 자리 정수 두 개를 입력 받아 각 자리 수를 교차 비교하여 같은 수 인지, 자리 값만 다른지,
# 하나의 수만 일치하는지, 또는 모두 일치하지 않는지를 구분하여 출력하는 script 작성하라
userInput = input("두 자리 정수 두개를 입력: ")
first, second = userInput.split()
first = int(first)
second = int(second)
firstFront = int(first / 10)
firstEnd = int(first % 10)
secondFront = int(second / 10)
secondEnd = int(second % 10)

if first == second:
    print("두 정수는 모두 {}로 같은 정수입니다." .format(first))
elif (firstFront == secondEnd) and (firstEnd == secondFront):
    print("{}, {}: 자리 값만 다른 정수입니다." .format(first, second))
elif (firstFront == secondFront) or (firstFront == secondEnd) or (firstEnd == secondFront) or (firstEnd == secondEnd):
    print("{}, {}: 하나의 숫자만 일치합니다." .format(first, second))
else:
    print("{}, {}: 일치하지 않는 정수입니다." .format(first, second))