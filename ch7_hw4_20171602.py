# by GEEE3, April 9, 2021
# 사용자로부터 숫자 월을 입력받아 그것에 대한 영문 이름을 출력하는 코드를 작성하시오

# 1. 2가지 버전으로 코드를 작성한다
# 2. 리스트 없이, if 조건문을 사용하여 작성하시오
print("***** if 조건문으로 작성 *****")
month = int(input("월을 입력하세요: "))
if month == 1:
    print("1월은 January입니다")
if month == 2:
    print("2월은 February입니다")
if month == 3:
    print("3월은 March입니다")
if month == 4:
    print("4월은 April입니다")
if month == 5:
    print("5월은 May입니다")
if month == 6:
    print("6월은 June입니다")
if month == 7:
    print("7월은 July입니다")
if month == 8:
    print("8월은 August입니다")
if month == 9:
    print("9월은 September입니다")
if month == 10:
    print("10월은 October입니다")
if month == 11:
    print("11월은 November입니다")
if month == 12:
    print("12월은 December입니다")

# 3. if 조건문 없이, 리스트를 사용하여 작성하시오
monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print("***** 리스트로 작성 *****")
month = int(input("월을 입력하세요: "))
print("{}월은 {}입니다" .format(month, monthList[month - 1]))