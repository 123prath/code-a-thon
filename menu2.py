#sub menu in perform transactions
from Operation import operations

def menu2():
    o = operations()
    while True:
        print("\nOPERATIONS : ")
        print("1.\tDeposit\n2.\tWithdraw\n3.\tChange Owner Name\n4.\tExit\n")
        choice = int(input("Choice >>> "))
        if choice == 1:
            o.deposit()
        elif choice == 2:
            o.withdraw()
        elif choice == 3:
            o.change()
        elif choice == 4:
            break
        else:
            print("Invalid choice")
            print("Please try Again")
            break
