from abc import abstractmethod,ABC
class Shape(ABC):
    @abstractmethod
    def printArea(self):
        return 0

class rectangle(Shape):
    type="Rectangel"
    sides=4
    def __init__(self,l,b):
        self.Lenth=l
        self.Breadth=b

    def printArea(self):
        return self.Lenth*self.Breadth

rect=rectangle(8,7)
print(rect.printArea())