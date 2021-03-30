# by GEEE3, March 24, 2021
# 수식을 입력 받아 연산 결과를 출력하는 script 작성하라
# (+, -, *, / 연산자만 구현, 그 외의 연산자는 허용하지 않는다는 메시지 출력)
calculator = input("수식 입력(예: 20 * 40) : ")
first, operation, second = calculator.split()
first = float(first)
second = float(second)

if operation == "+":
    print("{:.6f} {} {:.6f} = {:.6f}" .format(first, operation, second, first + second))
elif operation == "-":
    print("{:.6f} {} {:.6f} = {:.6f}" .format(first, operation, second, first - second))
elif operation == "*":
    print("{:.6f} {} {:.6f} = {:.6f}" .format(first, operation, second, first * second))
elif operation == "/":
    if second != 0:
        print("{:.6f} {} {:.6f} = {:.6f}" .format(first, operation, second, first / second))
    else:
        print("0.000000로 나누기를 수행할 수 없습니다")
else:
    print("{} 지원하지 않는 연산자입니다." .format(operation))