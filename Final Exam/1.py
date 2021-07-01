D = {'사과' : 100, '배' : 203, '오렌지' : 121, '바나나': 9}
fruit = list(D.items())
result = []
sum = 0

for i in range(len(D)):
    result.append(fruit[i][1])
    sum += int(fruit[i][1])

print("과일의 개수 리스트: {}" .format(result))
print("전체 과일의 개수: {}" .format(sum))