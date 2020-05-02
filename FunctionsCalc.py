import case.py

try:
  def main():
    Num1,Num2 = input_num()
    operation(Num1,Num2)
  

  def input_num():
    try:
      Num1=int(input("Enter Number 1: "))
      Num2=int(input("Enter Number 2: "))
      return (Num1,Num2)
    except:
      print("Invalid Number")

  def operation(Num1,Num2):
    try:
      ops=input("Enter operation(add/subtract/multiply/divide) to be performed: ")
      ops=ops.lower()
      if (ops=="add"):
        add(Num1,Num2)
      elif (ops=="subtract"):
        subtract(Num1,Num2)
      elif (ops=="multiply"):
        multiply(Num1,Num2)
      elif (ops=="divide"):
       division(Num1,Num2)
      else:
       print("Invalid Operation")
    except:
      print("Invalid Operation")


  def add(Num1,Num2):
    try:
      Output=Num1+Num2
      print("The sum of" , Num1, "and", Num2, "is",Output)
    except:
      print("Fucked up in addition")

  def subtract(Num1,Num2):
    try:
      Output=Num1-Num2
      print("The difference of" , Num1, "and", Num2, "is",Output)
    except:
      print("Fucked up in subtraction")

  def multiply(Num1,Num2):
    try:
      Output=Num1*Num2
      print("The product of" , Num1, "and", Num2, "is",Output)
    except:
      print("Fucked up in Multiplication")

  def division(Num1,Num2):
    try:
      Output=Num1/Num2
      print("The Division of" , Num1, "and", Num2, "is",Output)
    except:
      print("Fucked up in Division")


  main()

except:
  print("Code Failed")






