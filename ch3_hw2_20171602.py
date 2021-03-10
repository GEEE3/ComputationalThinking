# by GEEE3, March 10, 2021
# 3928원의 금액을 500원 동전으로 교환하고 나머지 금액을 100원 동전으로 교환하고자 한다
# 500웓 동전, 100원 동전의 개수를 계산하여 출력하고 남은 금액을 출력하는 script를 작성하라
money = 3928
numOf500 = money // 500
money %= 500
numOf100 = money // 100
remainder = money % 100

print("500원짜리 동전 :", numOf500, "개")
print("100원짜리 동전 :", numOf100, "개")
print("남은 금액 :", remainder, "원")