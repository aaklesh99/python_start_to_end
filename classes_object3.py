# class Employee():
#     no_of_leave=8
#     pass
#     def showdetails(self):
#          return f"Last name is {self.lastN} Salary is {self.salary} and Adderss is {self.add}"
#
# Akki = Employee()
# Aklesh = Employee()
#
#
# Akki.lastN = "Raj"
# Akki.salary = "300000"
# Akki.add="Sahrsa"

# Aklesh.lastN="Kumar"
# Aklesh.salary = "500000"
# Aklesh.add="Saharsa"
#
# print(Akki.showdetails())

#-----------------------Cunstructor-------------------------------

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
