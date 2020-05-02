#try is used to try a piece of code, any code with in "try" will be execute and on the basis of the code run

try:
  if var==null:
    print("Valuse is null")

# except is used to pass a message in case of a failure of code in try block
except:
  print("Error in code")

#  Finally is used as a teardown meathord where the code in finally will definately run even in case of failure of code in try
finally:
  print("teardown")