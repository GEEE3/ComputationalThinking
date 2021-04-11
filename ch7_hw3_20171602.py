# by GEEE3, April 9, 2021
# 리스트 method 중 append()를 사용하여 아래의 조건을 만족하는 script를 작성할 것

# 1. L = [1, 2, 3, 4, 5]에 새로 추가할 원소를 입력 받을 것
# 2. 추가할 원소의 데이터형은 정수로 제한
L = [1, 2, 3, 4, 5]
data = int(input("리스트 L에 추가할 data를 입력 : "))
L.append(data)
print(L)