for i in range (5):
    for j in range(6 - i):
        print(" ", end = '')
    for k in range(i * 2 + 1):
        print("*", end = '')
    print("")

for i in range (5):
    for j in range(4 - i):
        print(" ", end = '')
    for k in range(i * 2 + 5):
        print("*", end = '')
    print("")