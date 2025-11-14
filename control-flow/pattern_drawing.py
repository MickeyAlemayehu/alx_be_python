size = int(input("Enter the size of the pattern: "))
j =size

while j >= 0:
    for i in range(size, 0, -1):
        print('* ' ,end="" )
    j -= 1
    print()

