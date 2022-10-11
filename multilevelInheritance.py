class country():
    def __init__(self,Cname,CCap,nos):
        self.CountryName=Cname
        self.CountryCapital=CCap
        self.noOfState=nos
    # def cshow(self):
    #     return (f"Country name is{self.CountryName}, Capital is {self.CountryCapital}, No of State {self.noOfState}")

class state(country):
    def __init__(self,Sname,Scap,nod):
        super(state,self.__init__("India","New Delhi","28"))
        self.StateName=Sname
        self.StateCapital=Scap
        self.NoOfDistrict=nod

class District(state):
    def __int__(self):
        super(District, self).__int__("Bihar","Patna","38")
        self.NoOfBlock = 9

    def showDetails(self):
        return (f" Blocks are {self.NoOfBlock}")

    # Country
    # name is {self.CountryName}, Capital is {self.CountryCapital}, No
    # of
    # State
    # {self.noOfState}, State
    # name is {self.StateName}, \
    # capital is {self.StateCapital}, no.of
    # district
    # {self.NoOfDistrict} and

# det1=country("India","New Delhi","28")
# details1=det1.cshow()
# det2=state("Bihar","Patna","38")
# details2=det2.sshow()
# det3=District("9")
# details3=det3.showDetails()
# print(details1)
# print(details2)
dis=District('NoOfBlock')
print(dis)