class Base:
    x = 10  #Static variable
    def __init__(self):
        self.x = tuple([eval(x) for x in input("enter the range").split(',')]) #instance Variable
        Base.x = [eval(x) for x in input("enter the number").split(',')]
    def show_Base(self):
        print(self.x)
    def f1(self):
        print("base 1")
class Derived(Base):
    def __init__(self):
        self.y =[eval(x) for x in input("enter the sets").split(',')]
        super().__init__()
    def show_Derived(self):
        print(self.y)
    def f1(self):
        print("Derived")
obj = Derived()
obj.show_Derived()
obj.show_Base()
obj.f1()