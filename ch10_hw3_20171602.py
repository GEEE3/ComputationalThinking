# by GEEE3, May 21, 2021
# 다양한 개수의 정수를 입력 받아, 각 수가 양수인지 음수인지 구분하여
# 각각의 개수를 출력하는 script를 작성할 것

# 1. 입력으로부터 정수 리스트로 변환하는 것은 한 줄의 코드로 작성
# 2. 입력 받은 값 중 0은 무시
userInput = [int(x) for x in input("정수들을 입력:\n").split()]
counter = positive = negative = sum = 0

while counter < len(userInput):
    if userInput[counter] > 0:
        positive += 1
    elif userInput[counter] < 0:
        negative += 1
    sum += userInput[counter]
    counter += 1

if not userInput:
    print("입력한 숫자가 없습니다")
print("양수: {} 개, 음수: {} 개, 합계: {}" .format(positive, negative, sum))
