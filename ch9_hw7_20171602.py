# by GEEE3, May 12, 2021
# for와 range 함수를 이용하여 구구단 5단부터 8단까지 출력하시오
# 단 코드는 단 4줄만 사용할 것

for i in range(5, 9):
    for j in range(1, 10):
        print("{}" .format(i * j), end=" ")
    print("")