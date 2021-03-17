# by GEEE3, March 17, 2021
# 코드를 한 개의 파일에 구현하고 아래와 똑같이 출력하라

# 1. 변수에 10을 저장하고 변수의 값과 data type을 차례로 출력하라
data = 10
print(data, type(data), "\n")

# 2. 5의 루트 값을 구하여 소수점 5째 자리까지 반올림하여 출력하라
print("{}의 루트 값은: {:.5f}\n" .format(5, 5**(1/2)))

# 3. 'hello'를 변수에 저장하고 slicing으로 아래와 같이 출력하라
say = "hello"
say1 = say[::2]
say2 = say[::-1]
say3 = say[1::-1]
say4 = say[2:]
print("{}\n{}\n{}\n{}\n" .format(say1, say2, say3, say4))

# 4. 국어, 영어, 수학의 점수는 각각 80.3, 95.7, 73.2점이다 아래와 같이 출력하고 평균을 구하라
# 단, 소수점의 가로 위치는 모두 동일해야 한다
korean = 80.3
english = 95.7
math = 73.2
print("국어: {:6.2f}\n영어: {:6.2f}\n수학: {:6.2f}" .format(korean, english, math))
print("총점: {:5.2f}" .format(korean + english + math))
print("평균: {:8.4f}\n" .format((korean + english + math)/3))

# 5. 'These_functions_cannot_be_used_with_complex_numbers.' 과 같은 문자가 있다
# 여러가지 스트링 메소드를 사용하여 다음과 같이 출력하라
sen = "These_functions_cannot_be_used_with_complex_numbers."
rep = sen.replace("_", " ")
print("원래 문장:", sen)
print("수정한 문장:", rep)
print("{}는 {}번 나왔다." .format("a", rep.count("a")))
print("{}는 {}번 나왔다." .format("e", rep.count("e")))
print("{}는 {}번 나왔다." .format("u", rep.count("u")))
print("{}는 {}번 나왔다." .format("space", rep.count(" ")))
print("모두 대문자로 바꾸면:", rep.upper())