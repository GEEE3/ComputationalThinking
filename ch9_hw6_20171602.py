# by GEEE3, May 12, 2021
# 0보다 크고 10보다 작은 자연수 N을 입력 받아 삼각형 모양을 출력하는 프로그램을 작성하시오
userInput = int(input("Enter N (0 < N < 10) : "))

if userInput >= 10 or userInput <= 0:
    print("ERROR: N must be 0 < N < 10.")
elif userInput % 2 == 0:
    for i in range(1, userInput + 1):
        num = 1
        for j in range(i):
            print(num, end="")
            num += 1
        print("")
    for i in range(userInput):
        num = 1
        for j in range(userInput - i):
            print(num, end="")
            num += 1
        print("")
else:
    for i in range(1, userInput + 1):
        num = 1
        for j in range(i):
            print(num, end="")
            num += 1
        print("")
    for i in range(userInput - 1):
        num = 1
        for j in range(userInput - i - 1):
            print(num, end="")
            num += 1
        print("")