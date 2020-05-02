path="/Users/febin.t/Desktop/learn_python/"

txt = int(input("Enter Pin: "))
f= open(path + "create_first.txt","r+")
f.truncate()
f.write(str(txt))
f.close()

f2= open(path + "create_first.txt","r")
text = f2.read()
print(text)
