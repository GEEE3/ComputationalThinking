# by GEEE3, May 28, 2021

'''
사용자로부터 패스워드를 입력 받아 유효한 패스워드인지 검사하는 script를 작성할 것
아래의 조건에 맞게 코딩할 것

1. 패스워드 유효성 검사 기능은 함수로 구현할 것
2. 함수에서는 입력 받은 패스워드의 다음 조건을 체크
    a. 패스워드는 최소한 8자리 이상, 8자리 미만이면 False 반환
    b. 영문자, 숫자를 제외한 다른 문자가 있으면 False 반환
    c. 영문자로만 구성되었으면 False 반환
    d. 숫자로만 구성되었으면 False 반환
    e. 패스워드는 최소한 2개의 숫자를 가지고 있어야 함
3. 총 5번의 패스워드 유효성 검사, 유효하면 종료함
'''

def validation(userPassword):
    userPassword = str(userPassword)

    if len(userPassword) < 8:
        print("error! 8 글자 이상이어야 함")
        return False

    if userPassword.isalnum() != True:
        print("error! 영문자, 숫자로만 구성되어야 함")
        return False

    if userPassword.isalpha():
        print("error! 숫자도 포함되어야 함")
        return False

    if userPassword.isnumeric():
        print("error! 영문도 포함되어야 함")
        return False

    counter = 0
    for num in range(10):
        counter += userPassword.count(str(num))
    if counter < 2:
        print("error! 최소한 2개의 숫자를 포함해야 함")
        return False
    return True

for i in range(5):
    userPassword = input("Enter password: ")
    if(validation(userPassword) == True):
        print("Valid password")
        break
    else:
        print("Invalid password")