class Person:
    def __init__(self,n,a):
        self.name = n
        self.Age = a
class Student(Person):
    def __init__(self,n,a,r):
        self.RollNo = r
        Person.__init__(self,n,a)
class Teacher(Student):
    def __init__(self,n,a,s,sub):
        self.salary = s
        self.subject = sub
        Person.__init__(self,n,a)
class brightS(Student,Teacher):
    def __init__(self,p,n,a,r,s,sub):
        self.points = p
        Student.__init__(self,n,a,r)
        Teacher.__init__(self,n,a,s,sub)
obj = brightS(101,"Balkrishna",19,191,30000,"Physics")
print(obj.__dict__)