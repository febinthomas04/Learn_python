class test:
    try:
        def name(self):
            n=input("Enter name:")
            return n
            # print(n)
        def age(self):
            a=input("Enter age:")
            return a
            # print(a)
        def company(self):
            comp=input("Enter Company name:")
            return comp
        def salary(self):
            sal=int(input("Enter salary:"))
            return sal
            # print(sal)
        
    except expression as identifier:
        print("Failed in test Function")
        
class callAll:
    try:
        def feb(self):
            T = test()
            Name = T.name()
            Age = T.age()
            Salary = T.salary()
            Company = T.company()
            x = "My name is " + Name + " age is " + Age + " i work in " + Company + " and i earn " + str(Salary) + " per month "
            x = x.lower()
            print(x)
        
    except expression as identifier:
        print("Failed in CallAll Function")

call = callAll()
call.feb()
# print (ab)



