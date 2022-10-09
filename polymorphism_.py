class A:
    classvar1="I am in class A"
    def __init__(self):
        self.name="Akki"
        self.role="Student"
        self.roll="A23"

class B(A):
    classvar1 ="I am in class B "

    def __init__(self):
        super().__init__()
        self.name="Raj"
        self.role="Student"
        self.section="D2112"
        # super().__init__()
        # print(super().roll)

a=A()
b=B()

print(b.name,b.roll,b.role)