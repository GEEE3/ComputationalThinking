# 두 개의 문자열이 다음과 같이 주어졌을 때, 문자열에서 숫자 부분을 분리하여
# 앞의 문자 부분을 숫자만큼 반복 출력하는 script 작성 할 것

# 1. str1 = "Computer 4", str2 = "Science#5"
str1 = "Computer 4"
str2 = "Science#5"
str1 = str1[:8]
str2 = str2[:7]

# 2. "Computer" 문자열을 4번, "Science" 문자열을 5번 연속 출력
# 3. 두 개의 print() 함수 사용, * 연산자 사용
print(str1 * 4)
print(str2 * 5)