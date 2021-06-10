# by GEEE3, June 4, 2021

'''
동전 던지기 횟수를 입력 받아, 아래와 같이 정해진 횟수마다 앞면이 나온
확률을 출력하는 프로그램을 만들어라.

1. 1-10회는 매 횟수마다 출력하고, 11-100회는 10단위마다 출력
2. 함수는 던지기 횟수를 인수로 받으며 앞면이 나온 횟수를 반환한다
3. 동전 던지기는 random 모듈의 randint() 함수를 사용하여 0을 앞면, 1을 뒷면으로 설정
4. 마지막의 총 ~번 동전 던지기의 확률 출력은 main에서 한다
5. 반복문으로 코딩 가능한 부분은 반드시 반복문을 이용한다
'''

import random

def coinProbability(times):
    sum = 0

    for time in range(1, times + 1):
        sum += random.randint(0, 1)
        probability = int(((time - sum) / time) * 100)
        if time <= 10 or time % 10 == 0:
            print("{:3d} 번째까지 던지기에서 앞면이 나온 확률 : {:3d}%" .format(time, probability))
    
    print("")
    return probability

userInput = int(input("동전 던지기 시도 힛수를 입력(1 - 100) : "))
result = coinProbability(userInput)

print("*" * 45)
print("총 {}번 동전 던지기에서 앞면이 나올 확률: {}%" .format(userInput, result))