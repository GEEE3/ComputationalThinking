# by GEEE3, April 28, 2021
# 회사의 전체 직원 명단, 지각자 명단, 결석자 명단이 다음과 같을때
# 아래의 조건을 만족하는 결과를 출력하는 script 작성할 것
employee = {'공유', '고수', '보검', '태현', '종민', '세윤', '준호', '우종', '시우', '두준'}
late = {'우종', '보검'}
absent = {'종민', '우종', '보검', '두준'}

print("전체 사원 명단 :", employee)
print("지각자 명단 :", late)
print("결근자 명단 :", absent)

# 1. 지각과 결근을 한 번도 하지 않은 사원에게 보너스 지급
print("보너스 지급 대상자 명단 :", (employee - late) - absent)

# 2. 지각과 결근을 모두 한 사원에게 야근을 시킴
print("야근 대상자 명단 :", late & absent)

# 3. 1명 이상의 신입 사원 명단을 입력 받기
# 4. set 데이터형으로 처리할 것
userInput = input("신입사원 명단 입력 : ")
new = set(userInput.split())

if len(employee) + len(new) != len(employee | new):
    print("신입사원의 이름이 기존 사원의 이름과 중복")
print("전체 사원 명단 :", employee | new)