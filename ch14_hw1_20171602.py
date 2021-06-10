# by GEEE3, June 9, 2021

'''
L_In.txt를 읽어 첫 줄은 변수 Index에, 둘째 줄은 A에, 셋째 줄은 B에 저장힌다
A, B는 정수 리스트이며 출력은 L_Out.txt로 한다
L_Out.txt의 넷째 줄에서 A와 B리스트의 변수 index에 해당하는 원소를 서로 더하여 출력한다
readline()을 사용한다

L_In.txt
2
4 8 2 3 4 2
7 2 5 2 3 6 5
'''

FP_read = open("L_In.txt", 'r')
FP_write = open("L_Out.txt", 'w')

index = int(FP_read.readline())
first = FP_read.readline()
second = FP_read.readline()

A = []
B = []

for character in first:
    if character.isdecimal():
        A.append(int(character))
for character in second:
    if character.isdecimal():
        B.append(int(character))
result = A[index] + B[index]

FP_write.write("index = {}\n" .format(index))
FP_write.write("A = {}\nB = {}\n" .format(A, B))
FP_write.write("A[{}] + B[{}] = {}" .format(index, index, result))

FP_read.close()
FP_write.close()