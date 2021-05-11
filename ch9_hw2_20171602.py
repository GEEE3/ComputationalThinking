# by GEEE3, May 7, 2021
# range 함수를 이용하여 1부터 100까지의 숫자 중에서 짝수들을 원소로 하는 리스트 L을 생성한 후
# 그 중 8의 배수를 출력하는 script를 작성할 것
even = list(range(2, 100, 2))
result = []

for num in even:
    if num % 8 == 0:
        result.append(num)
        
print(result)