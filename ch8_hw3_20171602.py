# by GEEE3, April 28, 2021
# 과일 가게에서는 배, 자몽, 메론, 감을 판매하고 있으며 각 과일의 재고량과 단가를
# 사전 fruit = {'배': [2, 1000], '자몽': [1, 2000], '메론': [1, 8000], '감': [6, 800]}에 저장하고 있다
# 다음과 같이 결과를 출력하는 script 작성할 것
fruit = {'배': [2, 1000], '자몽': [1, 2000], '메론': [1, 8000], '감': [6, 800]}

# 1. 과일 이름을 입력 받아 판매하는 과일인 경우 재고에서 하나 뺌
choice = str(input("먹고 싶은 과일은? : "))
if fruit.get(choice) == None:
    print("{} 준비되어 있지 않습니다\n" .format(choice))
else:
    print("{} 맛있게 드세요\n" .format(choice))
    fruit.get(choice)[0] -= 1

# 2. 과일이 5개 미만인 경우는 과일당 재고가 5개는 되도록 구입하도록 함
print("각 과일 당 최소 5개는 되도록 구입합니다")
budget = 0

if int(fruit.get('배')[0]) < 5:
    budget += int(fruit.get('배')[1]) * (5 - fruit.get('배')[0])
if int(fruit.get('자몽')[0]) < 5:
    budget += int(fruit.get('자몽')[1]) * (5 - fruit.get('자몽')[0])
if int(fruit.get('메론')[0]) < 5:
    budget += int(fruit.get('메론')[1]) * (5 - fruit.get('메론')[0])
if int(fruit.get('감')[0]) < 5:
    budget += int(fruit.get('감')[1]) * (5 - fruit.get('감')[0])

print("구입에 필요한 총 금액은 : {} 원 입니다" .format(budget))