# by GEEE3, April 7, 2021
# 인덱싱을 사용하여 리스트 L = [[1, 2, 3], [4, 5], [6], [7, 8]]의
# 원소 리스트의 원소들을 제곱하여 그 합을 구하는 script 작성할 것

# 1. 제곱의 합들은 새로운 리스트에 저장하여 출력할 것
L = [[1, 2, 3], [4, 5], [6], [7, 8]]
square1 = pow(L[0][0], 2) + pow(L[0][1], 2) + pow(L[0][2], 2)
square2 = pow(L[1][0], 2) + pow(L[1][1], 2)
square3 = pow(L[2][0], 2)
square4 = pow(L[3][0], 2) + pow(L[3][1], 2)

# 2. 새로운 리스트에 저장할 때는 슬라이싱을 사용할 것
squared = list()
squared[0:0] =[square1, square2, square3, square4]
print(squared)