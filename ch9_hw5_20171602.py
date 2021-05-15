# by GEEE3, May 12, 2021

'''
다음 기능을 수행하는 프로그램을 작성하시오

1. 0보다 큰 정수 N1과 N2를 입력 받는다
2. N1보다 크거나 같고 N2보다 작거나 같은 모든 짝수의 합을 구하여 이를 출력한다

힌트
N1과 같거나 또는 크기가 하나 큰 짝수를 찾아 S에 저장하고
N2와 괕거나 또는 하나 큰 홀수를 찾아 E에 저장한다
S와 E 값을 range()의 인수로 사용하여 범위 내 짝수 합을 구한다
'''

userInput = input("두 자연수 N1과 N2를 입력하세요(0 < N1 <= N2) : ")
N1, N2 = userInput.split()
N1 = int(N1)
N2 = int(N2)

if N1 == N2:
    if N1 % 2 == 0:
        result = N1
    else:
        result = 0
else:
    if N1 % 2 == 0:
        S = N1
    else:
        S = N1 + 1

    if N2 % 2 == 0:
        E = N2 + 1
    else:
        E = N2

    even = list(range(S, E, 2))
    result = 0
    for num in even:
        result += num

print("크기가 {} 이상이고 {} 이하인 모든 짝수의 합은 {} 입니다." .format(N1, N2, result))