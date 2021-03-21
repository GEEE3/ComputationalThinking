# by GEEE3, March 19, 2021
# "Good words cost nothing" 문장에서 입력 받은 단어가 몇번 나오는지,
# 횟수를 출력하는 script 작성할 것 (출력시 포맷팅은 % operator 사용)
phrase = "Good words cost nothing"
word = input("찾는 단어 입력 : ")

print("Good words cost nothing 문장에서는 {} 단어가 {} 번 있습니다." .format(word, phrase.count(word)))