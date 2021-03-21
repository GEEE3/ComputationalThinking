# by GEEE3, March 19, 2021
# 두 점의 좌표 값을 순서대로 입력 받아(x1, y1, x2, y2) 다음과 같이 처리하는 script 작성할 것
import math

# 1. 한번의 input() 함수로 아래와 같이 네 개의 값을 받아 각 변수에 저장 할 것
num = input("두 점의 좌표값을 x1, y1, x2, y2 순서대로 입력 : ")
x1, y1, x2, y2 = num.split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

# 2. 두 점 사이의 거리를 계산해서 소수점 이하 2자리까지 출력
# 3. 거리 계산에 math 모듈의 sqrt() 함수 사용할 것
distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print("두 점 사이의 거리는 {:.2f} 입니다." .format(distance))

# 4. 두 점 사이의 거리가 5 이하인지 묻는 질문에 True, False로 대답하는 출력
print("두 점 사이의 거리는 5이하 입니까?", 5 >= distance)