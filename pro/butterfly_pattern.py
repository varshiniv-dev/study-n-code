length = int(input("Enter number of rows:"))
for i in range(length):
    for j in range(i):
        print('*', end='')
    for k in range(2*(length-i)):
        print('', end='')
    for l in range(i):
        print('*', end='')
    print()
for i in range(length):
    for j in range((length-1)-i+1):
        print('*', end='')
    for k in range(2*1):
        print('', end='')
    for l in range((length-1)-i*1):
        print('*', end='')
    print()
