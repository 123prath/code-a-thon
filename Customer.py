#to add new customer

import getconn
class customer:
    def __init__(self):
        self.mydb = getconn.getconn()
        self.mycur = self.mydb.cursor()

    def add_customer(self):
        while True:
            try:
                c_id = int(input("\nEnter Customer Id : "))
                f_name = input("Enter First Name : ")
                l_name = input("Enter Last Name : ")
                amt = int(input("Enter Amount : "))
                pswd = input("Enter Password : ")
                print()

                sql = "Insert Into Customer Values({},'{}','{}',{},'{}')".format(c_id, f_name, l_name, amt, pswd)
                self.mycur.execute(sql)

                if self.mycur.rowcount > 0:
                    self.mydb.commit()
                    print("Values has been Inserted")
                    print(f"Your Username is '{c_id}' and Password is '{pswd}'.")
                    print("Remember the Credentials and use it while Logging In\n")

                else:
                    self.mydb.rolback()
                    print("No Values Inserted")
                    continue

            except Exception as Err:
                print(Err)
                print("Failed")

            c = input("Do you wish to Enter more Records [y/n]: ")
            if c.lower() == "y":
                continue

            else:
                break

