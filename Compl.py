import calendar
kilom = int(input("enter the kilometer:"))
x = kilom/1.609
print(kilom,"kilometer convert to",x,"miles")

print("-------------convert celsius to farenheit----------------")
celsius = int(input("enter the celsius"))
f = (celsius*1.8)+32
print("Temperature is farenheit is:",f)

print("-----------Year & Calender------------")
y = int(input("Enter the year:"))
m = int(input("Enter the month"))
z = calendar.month(y,m)
print(z)

print("---------------Swap of two variable without any temp variable---------------")
x = int(input("enter the first No:"))
y = int(input("enter second No:"))
x = x+y
y = x-y
x = x-y
print("x:",x,"y:",y)