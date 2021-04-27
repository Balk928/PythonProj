dict = {}
while True:
    print("-------------Birthday App-------------")
    print("1:Show the Birthday")
    print("2:Enter the new Birthday list")
    print("-------------cmd calculator-----------")
    print("3:Addition")
    print("4:Subtraction")
    print("5:Multiplicaiton")
    print("6:exit")
    choice = int(input("enter the choice"))
    if choice == 1:
        if len(dict.keys()) == 0:
            print("Not a Birthday list")
        else:
            name = input("Enter the new Birthday list:")
            birth = dict.get(name, "No data found")
            print(birth)
    elif choice == 2:
        name = input("Enter friend name")
        date = input("Enter date of birth")
        dict[name] = date
        print("Birthday added")
    elif choice == 3:
        a, b = int(input("First No:")), int(input("Second No"))
        c = a + b
        print("Sum is ", c)
    elif choice == 4:
        a, b = int(input("First No:")), int(input("Second No"))
        c = a - b
        print("Subtraction is ", c)
    elif choice == 5:
        a, b = int(input("First No:")), int(input("Second No"))
        c = a * b
        print("Multiplication is ", c)
    elif choice == 6:
        break

    else:
        print("choice valid option")
