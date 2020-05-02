rows= int(input("Enter Number of Rows: "))
space= rows*2 -2
for var in range(0,rows):
    for s in range(0,space):
        print(end=" ")
    space=space-1
    for r in range(0,var+1):
        print("* ",end="")
    print("\r")