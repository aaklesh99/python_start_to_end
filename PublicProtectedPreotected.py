class test:
    var =9
    _protec=99
    __private=999

    def __init__(self,name):
        self.Name=name

    def show(self):
        return (f"name is {self.Name}")

# emp=test("Akki")
emp=test("Ram")
print(emp.show())
print(emp.var)
print(emp._protec)
print(emp._test__private)