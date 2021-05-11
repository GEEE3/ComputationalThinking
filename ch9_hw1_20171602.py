# by GEEE3, May 7, 2021
# 입력 받은 정수의 양수, 음수, 홀수, 짝수 여부를 출력하는 script 작성할 것

# 1. for문을 사용하여 숫자 하나씩 입력 받도록 함(10번의 입력을 받음)
# 2. 만약, 입력 받은 수가 0이면 루프를 종료
for i in range(10):
    userInput = int(input("Enter a number: "))

    if userInput > 0:
        if userInput % 2 == 0:
            print("{} : 양수, 짝수" .format(userInput))
        else:
            print("{} : 양수, 홀수" .format(userInput))
    elif userInput < 0:
        if userInput % 2 == 0:
            print("{} : 음수, 짝수" .format(userInput))
        else:
            print("{} : 음수, 홀수" .format(userInput))
    if userInput == 0:
        print("입력 받은 수가 0 입니다\n프로그램을 종료합니다")
        break