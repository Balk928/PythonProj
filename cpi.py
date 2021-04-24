class Student:
    def Record(self,Name,Roll,sem,branch):
        self.Name = Name
        self.Roll = Roll
        self.sem = sem
        self.branch = branch
t1 = Student()
t1.Record(str(input("Enter the Name")),int(input("Enter the RollNo")),int(input("Semester")),str(input("Enter Your Branch")))
print(t1.Name,t1.Roll,t1.sem,t1.branch)

