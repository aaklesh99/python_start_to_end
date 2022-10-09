class University:
    def __init__(self,Uname,Uadd,UVC):
        self.uniName=Uname
        self.uniAddress=Uadd
        self.univc=UVC

    def showUni(self):
        print(f"University name is{self.uniName}, University address is {self.uniAddress} and Voice Chancellor is {self.univc}")

class school():
    def __init__(self,scname,hos):
        self.SchoolName=scname
        self.HOS=hos

    def showSc(self):
        print(f"School name is {self.SchoolName} and Head of school is {self.HOS}")

class hod(University,school):
    Head_of_school = "girish Kumar"

    def showhod(self):
        print(f"Head of department is {self.Head_of_school}")



uni1=University("LPU","Jalandhar,Punjab","Ashok Mittal")
hos1=school("School of computer application","Balraj Sir")

print(uni1.showUni(),hos1.showSc(),hod.Head_of_school)
