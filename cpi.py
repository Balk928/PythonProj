class Student:
    def Record(self,Name,Roll,sem,branch):
        self.Name = Name
        self.Roll = Roll
        self.sem = sem
        self.branch = branch
    def marks(self,Daa,coreJava,FlA):
        self.Daa = Daa
        self.coreJava= coreJava
        self.FlA = FlA
t1 = Student()
t1.Record(str(input("Enter the Name")),int(input("Enter the RollNo")),int(input("Semester")),str(input("Enter Your Branch")))
print(t1.Name,t1.Roll,t1.sem,t1.branch)
t2 = Student()
t2.marks(70,70,70)
print("Daa:",t2.Daa,"CoreJava:",t2.coreJava,"FlA:",t2.FlA)
z = t2.Daa+t2.coreJava+t2.FlA//3
print("Average Marks is :",z)
