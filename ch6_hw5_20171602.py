# by GEEE3, March 31, 2021

'''
이차 방정식 근 제대로 구하기
알고리즘을 다음과 같이 수정한다
1. a, b, c를 입력 받는다
2. 판별식 D = b^2 - 4ac 를 계산한다
3. D > 0 이면
    a. D = sqrt(D)
    b. root1 = (-b + D) / 2a
    c. root2 = (-b - D) / 2a
    d. root1과 root2를 출력한다
4. D == 0 이면
    a. -b / 2a 를 계산하여 출력한다
5. D < 0 인 경우
    a. 근이 없음을 출력한다
'''

import math

userInput = input("Enter a, b, c : ")
a, b, c = userInput.split()
a = float(a)
b = float(b)
c = float(c)

D = (b ** 2) - (4 * a * c)

if D > 0:
    D = math.sqrt(D)
    root1 = (-b + D) / (2 * a)
    root2 = (-b - D) / (2 * a)
    print("root1 = {:.4f} and root2 = {:.4f}." .format(root1, root2))
elif D == 0:
    root = -b / (2 * a)
    print("single root = {:.4f}" .format(root))
else:
    print("no root exists.")