row = int(input("Enter value for x: "))
for i in range(row):
    num=i*4+1
    for j in range(row):
        print(num,end=" ")
        num=num+2
        
    print()