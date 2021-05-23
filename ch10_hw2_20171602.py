# by GEEE3, May 21, 2021
# 구하려는 소수의 개수를 입력 받아, 개수만큼의 소수를 구하여 출력하는 script를 작성할 것
userInput = int(input("구하려는 소수의 개수를 입력: "))
counter = 0
num = 2

while counter < userInput:
    divider = 2
    primeFlag = True
    while divider < num:
        if num % divider == 0:
            primeFlag = False
            break
        divider += 1
    if primeFlag == True:
        counter += 1
        print(num)
    num += 1

print(counter, "개의 소수를 찾았습니다")