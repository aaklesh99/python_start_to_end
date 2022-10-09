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

class Programmer(Employee):
    def __init__(self,lastN,salary,add,language):
        self.lastN=lastN
        self.salary=salary
        self.add=add
        self.languages=language
    def showProdetails(self):
        return f"Last name is {self.lastN}, Salary is {self.salary}, Adderss is {self.add} and the language are{self.languages}"


Akki = Employee("Raj","64534","Saharsaa")
Akki.changeleave(32)
Mohan=Employee.from_dash("Aklesh-67587-Bihar")
# print(Akki.salary)
# print(Mohan.salary)
print(Mohan.salary)
Aklesh=Programmer("Kumar","87879","Saharsa",["CPP","JS","Flutter"])
print(Aklesh.showProdetails())


#----------------------------------Static--------------------------------#