class Employee():
    no_of_leave=8
    pass
Akki = Employee()
Aklesh = Employee()

Akki.lastN = "Raj"
Akki.salary = "300000"
Akki.add="Sahrsa"

Aklesh.lastN="Kumar"
Aklesh.salary = "500000"
Aklesh.add="Saharsa"
print(Akki.__dict__)
print(" ",Akki.lastN,Akki.salary,Akki.add,Akki.no_of_leave,"\n",Aklesh.lastN,Aklesh.salary,Aklesh.add,Aklesh.no_of_leave)