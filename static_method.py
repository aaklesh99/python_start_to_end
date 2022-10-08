class Employee():
    no_of_leave=8
    pass
    def __init__(self,lastN,salary,add):
        self.lastN=lastN
        self.salary=salary
        self.address=add

    def showdetails(self):
          return f"Last name is {self.lastN} Salary is {self.salary} and Adderss is {self.add}"
    @classmethod
    def changeleave(cls,newleave):
        cls.no_of_leave=newleave
    @classmethod
    def from_dash(cls,string):
        nya = string.split("-")
        print(nya)
        return cls(nya[0],nya[1],nya[2])
        # return cls(*string.split(("-")))
    @staticmethod
    def printgood(str):
        print(f"This is good name {str}")




Akki = Employee("Raj","64534","Saharsaa")
Akki.changeleave(32)
Mohan=Employee.from_dash("Aklesh-67587-Bihar")
# print(Akki.salary)
# print(Mohan.salary)
print(Mohan.salary)
Mohan.printgood("Banana")



#----------------------------------Static--------------------------------#