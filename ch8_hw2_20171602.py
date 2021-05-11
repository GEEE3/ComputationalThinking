# by GEEE3, April 28, 2021
# D = {'c': 7, 'f': 3, 'a': 5} 인 사전에서 (key, value) 쌍의 데이터를 구해
# 오름차순으로 정렬하여 다음과 같이 결과를 출력하는 script 작성할 것 (튜플 데이터는 리스트에 저장)
D = {'c': 7, 'f': 3, 'a': 5}
paired = D.items()
paired = list(paired)

result = sorted(paired)
print("After sort:", result)