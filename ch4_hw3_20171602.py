# by GEEE3, March 17, 2021
# sample = "abcABCdEFaBCDeFAbC" 문자열이 주어졌을 때,
# 대소문자 구분 없이 "abc", "def" 문자열이 처음 시작하는 인덱스, 반복 횟수를
# 다음과 같이 출력하는 script 작성할 것(출력시 포맷팅은 %operator 사용)
sample = "abcABCdEFaBCDeFAbC"
sample = sample.lower()
key1 = "abc"
key2 = "def"

print('"abc 문자열: {} 인덱스, {} 번 존재"' .format(sample.find(key1), sample.count(key1)))
print('"def 문자열: {} 인덱스, {} 번 존재"' .format(sample.find(key2), sample.count(key2)))