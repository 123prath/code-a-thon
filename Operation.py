#operations like deposit,withdraw,change owner name
from Customer import customer


class operations(customer):
    def __init__(self):
        customer.__init__(self)

    def deposit(self):

        c_id = int(input("Enter ID of Account where Money is to be Deposited: "))
        amount = int(input("Enter the Amount you wish to deposit : "))

        sql = "select amt from customer where c_id = {}".format(c_id)
        self.mycur.execute(sql)

        r = self.mycur.fetchall()

        ls = []
        for i in r:
            ls.append(i[0])

            print(f"\nOld Balance was {ls[0]}")
            sql = "Update customer set amt = {} + {} where c_id = {}".format(ls[0], amount, c_id)
            self.mycur.execute(sql)

            if self.mycur.rowcount > 0:
                self.mydb.commit()
                print("Records updated Successfully\nCheck Balance to know Updated Balance\n")
            else:
                self.mydb.rollback()
                print("No Records were Updated")



    def withdraw(self):
        try:
            c_id = int(input("Enter Customer ID : "))
            amount = int(input("Enter the Amount you wish to Withdraw : "))

            sql = "select amt from customer where c_id = {}".format(c_id)
            self.mycur.execute(sql)

            r = self.mycur.fetchall()

            ls = []
            for i in r:
                ls.append(i[0])
                a = ls[0]

                if a >= amount:
                    print(f"\nOld Amount was {a}")
                    sql = "Update customer set amt = {} - {} where c_id = {}".format(a, amount, c_id)
                    self.mycur.execute(sql)

                    if self.mycur.rowcount > 0:
                        self.mydb.commit()
                        print("Records updated Successfully\nCheck Balance to know Updated Balance\n")
                    else:
                        self.mydb.rollback()
                        print("No Records were Updated")

                else:
                    print("\nTRANSACTION UNSUCCESSFUL")
                    print(f"Balance is '{a}' and Withdrawal amount is '{amount}'")
                    print("Withdrawal amount is more than Balance\n")

        except Exception as err:
            print("Something Went Wrong. Please Try Again", err)

    def change(self):
        c_id = int(input("Enter your customer id : "))
        new_name = input("Enter new first name : ")
        new_last = input("Enter new last name : ")

        sql = "Update customer set f_name= '{}'  where c_id = {}".format(new_name, c_id)
        self.mycur.execute(sql)

        if self.mycur.rowcount > 0:
            self.mydb.commit()
        else:
            self.mydb.rollback()


        sql = "Update customer set l_name = '{}' where c_id = {}".format(new_last, c_id)
        self.mycur.execute(sql)

        if self.mycur.rowcount > 0:
            self.mydb.commit()
        else:
            self.mydb.rollback()

        print("Your request has been successfully completed...")
        print("New owner name is {} {}".format(new_name,new_last))