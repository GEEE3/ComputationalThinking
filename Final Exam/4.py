import random

def pow2(list1):
    list2 = []
    for i in range(10):
        list2.append(list1[i] ** 2)
    
    return list2

list1 = []
for i in range(10):
    list1.append(int(random.randint(-10, 10)))

list2 = pow2(list1)
print("함수에 의해 가공된 리스트: ", list2)
print("랜덤(-10~10)으로 생성된 리스트: ", list1)