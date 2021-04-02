# by GEEE3, March 31, 2021

'''
판별식이 거의 0에 가까우면 중근으로 판정하는 알고리즘
0. bound = 1.0e-8
1. a, b, c를 입력 받는다
2. 판별식 D = b^2 - 4ac 를 계산한다
3. abs(D) <= bound 이면
    a. -b / 2a 를 계산하여 출력한다
4. D > 0 이면
    a. D = sqrt(D)
    b. root1 = (-b + D) / 2a
    c. root2 = (-b - D) / 2a
    d. root1과 root2를 출력한다
5. D < 0 인 경우
    a. 근이 없음을 출력한다
'''

import math

userInput = input("Enter a, b, c : ")
a, b, c = userInput.split()
a = float(a)
b = float(b)
c = float(c)
bound = 1.0e-8

D = (b ** 2) - (4 * a * c)

if abs(D) < bound:
    root = -b / (2 * a)
    print("single root = {:.4f}" .format(root))
elif D > 0:
    D = math.sqrt(D)
    root1 = (-b + D) / (2 * a)
    root2 = (-b - D) / (2 * a)
    print("root1 = {:.4f} and root2 = {:.4f}." .format(root1, root2))
else:
    print("no root exists.")