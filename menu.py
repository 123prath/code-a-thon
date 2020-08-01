#main menu of banking application
from Customer import customer
from menu2 import menu2

while True:
    print("*" * 25 + "--DETROIT UNITED BANK--" + "*" * 25)
    print("1. Add Customer\n2. Perform Transaction\n3.Exit")
    ch = int(input("Choice >>> "))
    c = customer()
    if ch == 1:
        c.add_customer()
    elif ch == 2:
        menu2()
    elif ch == 3:
        break
    else:
        print("Invalid Choice")
        break
