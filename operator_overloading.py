class Employee:

    def __init__(self,name,salary,workighr):
        self.name=name
        self.salary=salary
        self.workingHour=workighr
    def showdetails(self):
        print(f"Name {self.name}, Salary is {self.salary} and workig hour {self.workingHour}")

    def __add__(self, other):
        return self.salary + other.salary
    def __repr__(self):
        return (f"Employee('{self.name}', {self.salary} ,'{self.workingHour}')")
    def __str__(self):
        return print(f"Name {self.name}, Salary is {self.salary} and workig hour {self.workingHour}")


emp1=Employee("Akki Raj",678987,8)
emp2=Employee("Aklesh kumar",34243,9)
emp1.showdetails()
emp2.showdetails()
print(emp1+emp2)
print(repr(emp2))
print(str(emp1))
