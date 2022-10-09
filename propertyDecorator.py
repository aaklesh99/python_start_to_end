class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@mail.com"

    def show(self):
        return f"first name is {self.fname} {self.lname} and email is {self.email}"
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not exits,please set it using setter"
        return f"{self.fname}.{self.lname}@mail.com"

    @email.setter
    def email(self,string):
        print("Setting now...")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None


emp1=Employee("Akki", "Raj")
print(emp1.show())
emp1.fname="Aklesh"
print(emp1.show())
print(emp1.email)
emp1.email="Akki.raj@gmail.com"
print(emp1.email)
print(emp1.fname)
print(emp1.lname)

del emp1.email
print(emp1.email)