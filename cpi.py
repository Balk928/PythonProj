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
    def f3(self,emp_id,Emp_Name,Salary):
        self.emp_id = emp_id
        self.Emp_Name = Emp_Name
        self.Salary = Salary

t1 = Student()
t1.Record(str(input("Enter the Name")),int(input("Enter the RollNo")),int(input("Semester")),str(input("Enter Your Branch")))
print(t1.Name,t1.Roll,t1.sem,t1.branch)
t2 = Student()
t2.marks(70,70,70)
print("Daa:",t2.Daa,"CoreJava:",t2.coreJava,"FlA:",t2.FlA)
z = t2.Daa+t2.coreJava+t2.FlA//3
print("Average Marks is :",z)
t3 = Student()
t3.f3(input("EmployeeId:"),input("Enter Name:"),float(input("Salary:")))
print(t3.emp_id,t3.Emp_Name,t3.Salary)

