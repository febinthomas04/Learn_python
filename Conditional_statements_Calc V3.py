Num1 = int(input("Enter Number 1 : ")) 
Num2 = int(input("Enter Number 2 : "))
Operation = input("Enter operation Add/Multiply/Subtract/Divide : ")
if(Operation=="Add"):
    Num3=Num1+Num2
    print ("Sum is" , Num3)
elif(Operation=="Multiply"):
    Num3=Num1*Num2
    print ("Product is ",Num3)
elif(Operation=="Subtract"):
    if(Num1>Num2):
        Num3=Num1-Num2
        print ("Difference is ",Num3)
    else:
        print (Num2 ,"is Greater than" , Num1, "so Difference will be negative")
        Num3=Num1-Num2
        print ("Difference is ",Num3)
elif(Operation=="Divide"):
    if(Num1==0):
        print ("Number Cannot be 0")
    elif(Num2==0):
        print ("Number Cannot be 0")
    else:
        Num3=int(Num1/Num2)
        print ("Division is ",Num3)
else:
    print ("Invalid Operation")



