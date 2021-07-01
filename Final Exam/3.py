def isPrimary(num):
    flag = 0

    for i in range(1, num - 1):
        if num % (i + 1) == 0:
            flag += 1
    
    if flag != 0:
        return True
    else:
        return False

def returnSum(num):
    result = 0

    for i in range(num):
        if num % (i + 1) == 0:
            result += (i + 1)

    return result



print("입력한 수까지 1과 소수를 제외한 수의 약수의 합을 구합니다.")
userInput = int(input("양의 정수를 입력하세요: "))

for i in range(userInput):
    if isPrimary(i + 1):
        print("{}의 약수의 합은 {}입니다." .format(i + 1, returnSum(i + 1)))