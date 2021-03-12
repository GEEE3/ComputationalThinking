# s1 = "Sogang University" 문자열이 주어졌을 때, s1에 대한 슬라이싱을 이용하여
# s2에 "Sogang", s3에 "University", s4에 "gnagoS"를 저장하고 아래와 같이 출력하라
s1 = "Sogang University"
s2 = s1[:6]
s3 = s1[7:]
s4 = s2[::-1]

print("s1은", s1)
print("s2는", s2)
print("s3은", s3)
print("s4는", s4)