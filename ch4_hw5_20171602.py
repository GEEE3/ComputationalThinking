# by GEEE3, March 17, 2021
# num = 3.1415926; x = "123"; y = "abc" 변수에 값을 주고,
# 다음과 같은 조건과 주석의 조건을 만족하게 출력하시오

# 1. 주어진 변수만 사용하여 출력할 것
num = 3.1415926
x = "123"
y = "abc"

# 2. 4개의 print() 문의 출력 형식을 지킬 것
# 3. 문자열의 메소드 format()을 사용하여 출력할 것
print("{0[2]}, {0[0]}, {0[1]}" .format(x))
print("{:10.2f}" .format(num))
print("{:10d}" .format(123))
print("{0:<10}" .format(y.ljust(10)))