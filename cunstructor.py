class Employee():
    no_of_leave=8
    pass
    def __init__(self,lastN,salary,add):
        self.lastN=lastN
        self.salary=salary
        self.address=add

    def showdetails(self):
          return f"Last name is {self.lastN} Salary is {self.salary} and Adderss is {self.add}"


Akki = Employee("Raj","64534","Saharsaa")
print(Akki.salary)
