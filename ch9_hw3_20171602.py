# by GEEE3, May 7, 2021
# 다음과 같이 값들이 주어졌을 때
# A = [4, 8, 2, 3, 4, 2]
# B = [7, 2, 5, 2, 3, 6, 5]
# 리스트 A와 B에 공통으로 있는 원소들을 오름차순으로 정렬한 새로운 리스트를 만들어 출력할 것
A = [4, 8, 2, 3, 4, 2]
B = [7, 2, 5, 2, 3, 6, 5]
temp1 = []
temp2 = []

for num1 in A:
    if num1 in B:
        temp1.append(num1)

for num2 in temp1:
    if num2 not in temp2:
        temp2.append(num2)

result = sorted(temp2)
print(result)