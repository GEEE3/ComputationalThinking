# by GEEE3, May 12, 2021

'''
모집단의 표준 편차 구하기
다음과 같은 pseudocode를 프로그래밍 하자
1. input data[0, N - 1]
2. M2 = E2 = 0
3. for d in data
4.  M2 += d ** 2
5.  E2 += d
6. M2 = M2 / N
7. E2 = (E2 / N) ** 2
8. std_dev = sqrt(M2 - E2)
9. print std_dev
'''

import math
userInput = [float(x) for x in input("Enter data :\n").split()]

for i in range(len(userInput)):
    userInput[i] = float(userInput[i])
    
M2 = E2 = 0
for i in range(len(userInput)):
    M2 += userInput[i] ** 2
    E2 += userInput[i]

M2 = M2 / len(userInput)
E2 = (E2 / len(userInput)) ** 2
std_dev = math.sqrt(M2 - E2)
print("{:.5f}" .format(std_dev))