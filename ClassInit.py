class test:
    try:

        def __init__(self,name,age,salary,company):
            self.name2=name
            self.age2=age
            self.salary2=salary
            self.company2=company

        def namef(self):
            print("My name is " + self.name2 + " age is " + str(self.age2) + " i work in " + self.company2 + " and i earn " + str(self.salary2) + " per month ")
        
    except expression as identifier:
        print("Failed in test Function")
        

class babe:
    def name(self):
            n=input("Enter name:")
            return n
            # print(n)
    def age(self):
        a=int(input("Enter age:"))
        return a
        # print(a)
    def company(self):
        comp=input("Enter Company name:")
        return comp
    def salary(self):
        sal=int(input("Enter salary:"))
        return sal
        # print(sal)


class callAll:
    try:
        def feb(self):
            b=babe()    
            Name = b.name()
            Age = b.age()
            Salary = b.salary()
            Company = b.company()
            Te = test(Name,Age,Salary,Company)
            # Te=test("febin","25",50000,"greyorange")
            Famo=Te.namef()


            # x = "My name is " + Name + " age is " + Age + " i work in " + Company + " and i earn " + str(Salary) + " per month "
            # x = x.lower()
            # print(x)
        
    except expression as identifier:
        print("Failed in CallAll Function")

call = callAll()
call.feb()
# print (ab)



