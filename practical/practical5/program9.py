row = int(input("Enter value for x: "))
for i in range(row):
    num=i*2+1
    for j in range(row):
        print(num,end=" ")
        num+=2
    print()