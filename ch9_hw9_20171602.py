# by GEEE3, May 12, 2021
# 1. 학생의 점수를 입력하여 학점을 주는 프로그램을 작성하시오
# 2. 90점 이상은 A, 70점까지는 B, 50점 까지는 C, 나머지는 F
userInput = input("성적들을 입력하세요 : ")
userInput = userInput.split()

for i in range(len(userInput)):
    userInput[i] = int(userInput[i])

student = 0
for num in userInput:
    student += 1
    if num >= 90:
        print("{}번 학생의 성적은 A입니다." .format(student))
    elif num >= 70:
        print("{}번 학생의 성적은 B입니다." .format(student))
    elif num >= 50:
        print("{}번 학생의 성적은 C입니다." .format(student))
    else:
        print("{}번 학생의 성적은 F입니다." .format(student))