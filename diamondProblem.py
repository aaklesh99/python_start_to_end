class A():
    def met(self):
        print("I am in A")
class B(A):
    def met(self):
        print("I am in B")

class C(A):
    def met(self):
        print("I am in c")
class D(B,C):
    pass
    # def met(self):
    #     print("I am in D")

a=A()
b=B()
c=C()
d=D()
print(d.met())