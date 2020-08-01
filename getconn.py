#for making connection with database
#Database (detroit united bank)-[c_id,f_name,l_name,amt,pswd]
import mysql.connector as my


def getconn():
    mydb = my.connect(host="localhost", user="root", passwd="", database="detroit united bank")

    if mydb:
        print("Server Connected")
        return mydb
