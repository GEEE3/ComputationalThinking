# by GEEE3, May 28, 2021
# 메인에서 입력 받은 문자열을 넘겨 받아, 포함된 문자의 개수를 각각 세어 반환하는 script를 작성할 것
# 아래의 조건에 맞게 코딩할 것
# 1. 대소문자 구분을 하지 않음
# 2. 빈칸은 무시
# 3. 반환 받은 문자의 개수 정보는 메인에서 출력할 것

def letterCounter(userInput, letter):
    userInput = str(userInput)
    return userInput.count(letter)

userInput = input("문자열 입력 : ")
userInput = userInput.lower()
userInput = userInput.replace(' ', '')
counter = []

for letter in userInput:
    if letter not in counter:
        counter.append(letter)

        result = letterCounter(userInput, letter)
        print("{} : {}" .format(letter, result))