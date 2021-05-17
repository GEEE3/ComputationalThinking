# by GEEE3, May 12, 2021
# 아래와 같은 별을 출력하라

for i in range(1, 6):
    flag = 0
    for j in range(i * 2 - 1):
        if flag == 0:
            print(" " * (5 - i), end='')
            flag = 1
        print("*", end='')
    print("")