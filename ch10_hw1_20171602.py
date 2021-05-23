# by GEEE3, May 21, 2021
# 임의의 정수들을 입력 받아 합계와 평균을 계산하여 출력하는 script를 작성할 것
# 0 이 입력되면 더 이상의 입력을 받지 않고 결과를 출력하며, 출력 시 입력 받은 정수들도 함께 출력
userInput = 0
inputList = []
sum = 0

# 1. while 문 사용
# 2. 입력 받은 값은 리스트에 저장
# 3. 입력문은 한번 사용
while True:
    userInput = int(input("정수를 입력 (0을 입력하면 종료) : "))
    if userInput != 0:
        inputList.append(userInput)
    else:
        break
    
for i in range(len(inputList)):
    sum += inputList[i]

print("입력한 정수 리스트 :", inputList)
print("합계 :", sum)
print("평균 :", sum / len(inputList))