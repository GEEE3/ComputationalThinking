# by GEEE3, June 4, 2021
# 수식을 입력 받아 연산 결과를 출력하는 script 작성하라
# (+, -, *, / 연산자만 구현, 그 외의 연산자는 허용하지 않는다는 메시지 출력)
# 1. 각 연산자에 해당하는 함수를 구현할 것
# 2. 메인에서는 연산자에 따라 함수를 호출하며, 계산 결과를 반환 받아 출력할 것

def addition(first, second):
    return first + second

def subtraction(first, second):
    return first - second

def multiplication(first, second):
    return first * second

def division(first, second):
    return first / second

calculator = input("수식 입력(예: 20 * 40) : ")
first, operation, second = calculator.split()
first = float(first)
second = float(second)
flag = 0

if operation == "+":
    result = addition(first, second)
elif operation == "-":
    result = subtraction(first, second)
elif operation == "*":
    result = multiplication(first, second)
elif operation == "/":
    if second != 0:
        result = division(first, second)
    else:
        print("0.000000 로 나누기를 수행할 수 없습니다")
        flag = 1
else:
    print("{} 지원하지 않는 연산자입니다." .format(operation))
    flag = 1
    
if flag == 0:
    print("{:.6f} {} {:.6f} = {:.6f}" .format(first, operation, second, result))