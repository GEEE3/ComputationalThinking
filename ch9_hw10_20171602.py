# by GEEE3, May 12, 2021
# 아래와 같은 구구단을 출력하라

for i in range(2, 10):
    for j in range(1, i + 1):
        print("{}*{}={:2d}" .format(i, j, i * j), end=' ')
    print("")