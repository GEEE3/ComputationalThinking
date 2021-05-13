# by GEEE3, March 31, 2021

'''
이차 방정식의 근 구하기
문제를 다음과 같이 분해하여 근을 구한다
1. a, b, c를 입력 받는다
2. 판별식 D = b^2 - 4ac 를 계산한다
3. D = sqrt(D)
4. root1 = (-b + D) / 2a
5. root2 = (-b - D) / 2a
6. root1과 root2를 출력한다
'''

import math

userInput = input("Enter a, b, c : ")
a, b, c = userInput.split()
a = float(a)
b = float(b)
c = float(c)

D = (b ** 2) - (4 * a * c)
D = math.sqrt(D)
root1 = (-b + D) / (2 * a)
root2 = (-b - D) / (2 * a)

print("root1 = {:.4f} and root2 = {:.4f}." .format(root1, root2))