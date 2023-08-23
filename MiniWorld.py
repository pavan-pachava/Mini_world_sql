import subprocess as sp
import pymysql
import pymysql.cursors

def addCustomer():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter Customer's details: ")
        row["ID_No"] = input("ID Number : ")
        name = input("Name : ")
        row["name"] = name
        row["sold_to"] = input("Sold to : ")
        

        query = "INSERT INTO CUSTOMER(ID_Number, Customer_name, Sold_to) VALUES('%s', '%s', '%s')" % (row["ID_No"], row["name"], row["sold_to"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def addCar():
    try:
        row = {}
        print("Enter Car's details: ")
        row["Serial_number"] = int(input("Serial Number : "))
        row["Car_name"] = input("Name : ")
        row["Car_year"] = int(input("Manufacture Year : "))
        row["Price"] = input("Price : ")
        
        #row["Distributor_name"] = input("Distributor : ")
        #row["Manufacturer_name"] = input("Manufacturer : ")
        #row["ID_Number"] = input("ID Number : ")
        #row["Store_name"] = input("Store : ")
        #row["Car_ID"] = row["Serial_number"]

        query1 = "INSERT INTO car(Serial_number, Car_name, Car_year, Price) VALUES('%s', '%s', '%s', '%s')" % (row["Serial_number"], row["Car_name"], row["Car_year"], row["Price"])
        #query2 = "INSERT INTO car_details(Distributor_name, Manufacturer_name, ID_Number, Store_name, Car_ID) VALUES('%s', '%s', '%s', '%s', '%s')" % (row["Distributor_name"], row["Manufacturer_name"], row["ID_Number"], row["Store_name"], row["Car_ID"])

        print(query1)
        #print(query2)
        cur.execute(query1)
        con.commit()
        #cur.execute(query2)
        #con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def addPincode():
    # area_assigned
    try:
        row = {}
        print("Enter Pincodes for store: ")
        row["Store_name"] = (input("Store : "))
        x = int(input("Number of pincodes to add : "))
        for i in range(x):
            row["Pincode'%s'" %(i)] = int(input("Pincode : "))

            query1 = "INSERT INTO area_assigned(Store_name, Pincode) VALUES('%s', '%s')" % (row["Store_name"], row["Pincode'%s'" %(i)])
            
            print(query1)
            cur.execute(query1)
            con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def addAward():
    try:
        row = {}
        print("Enter Award details: ")
        row["Award_name"] = (input("Award : "))
        row["Year"] = int(input("Year : "))
        row["Award_reason"] = (input("Award Description : "))
        row["Receiver"] = input("Receiver : ")

        query1 = "INSERT INTO award(Award_name, Year, Award_reason, Receiver) VALUES('%s', '%s', '%s', '%s')" % (row["Award_name"], row["Year"], row["Award_reason"], row["Receiver"])
        
        print(query1)
        cur.execute(query1)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def addStore():
    try:
        row = {}
        print("Enter Store details: ")
        row["Store_name"] = (input("Store name : "))
        row["Area"] = (input("Area : "))
        row["City"] = (input("City : "))
        row["State"] = (input("State : "))
        row["Country"] = (input("Country : "))

        query1 = "INSERT INTO store(Store_name, Area, City, State, Country) VALUES('%s', '%s', '%s', '%s', '%s')" % (row["Store_name"], row["Area"], row["City"], row["State"], row["Country"])
        
        print(query1)
        cur.execute(query1)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def changeSell():
    try:
        row = {}
        print("Enter Seller details: ")
        row["ID_Number"] = int(input("Seller ID : "))
        row["Sold_to"] = int(input("Buyer ID : "))
        row["Car_ID"] = int(input("Car ID : "))

        query1 = "UPDATE car_owned SET ID_Number = '%s' WHERE ID_Number = '%s'" % (row["Sold_to"], row["ID_Number"])
        query2 = "UPDATE customer SET Sold_to = '%s' WHERE ID_Number = '%s'" % (row["Sold_to"], row["ID_Number"])
        # query3 = "UPDATE customer SET Sold_to = NULL WHERE ID_Number = '%s'" % (row["Sold_to"], row["ID_Number"])
        
        print(query1)
        print(query2)
        # print(query3)
        cur.execute(query1)
        con.commit()
        cur.execute(query2)
        con.commit()
        # cur.execute(query3)
        # con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def changeDisplayStore():
    try:
        row = {}
        print("Enter Car and Store details : ")
        row["Car_ID"] = int(input("Car ID : "))
        row["Store_name"] = input("Updated Store : ")

        query1 = "UPDATE car_details SET Store_name = '%s' WHERE Car_ID = '%s'" % (row["Store_name"], row["Car_ID"])
        # query3 = "UPDATE customer SET Sold_to = NULL WHERE ID_Number = '%s'" % (row["Sold_to"], row["ID_Number"])
        
        print(query1)
        # print(query3)
        cur.execute(query1)
        con.commit()
        # cur.execute(query3)
        # con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def deletecustomer():
    try:
        row = {}
        print("Enter Customer details to delete : ")
        row["ID_Number"] = int(input("Customer ID : "))

        query1 = "DELETE FROM customer WHERE ID_Number='%s' " % (row["ID_Number"])
        query2 = "DELETE FROM car_owned WHERE ID_Number='%s' " % (row["ID_Number"])
        query3 = "UPDATE car_details SET ID_Number = NULL WHERE ID_Number='%s' " % (row["ID_Number"])
        
        print(query1)
        print(query2)
        print(query3)
        cur.execute(query1)
        con.commit()
        cur.execute(query2)
        con.commit()
        cur.execute(query3)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def searchPincode():
    try:
        row = {}
        pin = int(input("Pincode (initial numbers): "))
        pin1=pin+1
        while (pin<100*000):
            pin*=10
            pin1*=10

        query1 = "SELECT DISTINCT Store_name AS Stores WHERE Pincode >'%s' AND Pincode <'%s'" % (pin, pin1)
        
        print(query1)
        cur.execute(query1)
        result=cur.fetchall()
        con.commit()
        
        print("Stores Serving the Area : ", result["Stores"])

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def carSold():
    try:
        row = {}
        store = (input("Store : "))
        comp = input("Company : ")

        query1 = "SELECT DISTINCT car.Car_name AS Cars FROM car, car_details WHERE car_details.Store_name='%s' AND car_details.Manufacturer_name='%s' AND car_details.Car_ID=car.Serial_number" % (store, comp)
        
        print(query1)
        cur.execute(query1)
        result=cur.fetchall()
        con.commit()
        
        print("Cars with specified details : ", result["Cars"])

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def car():
    try:
        row = {}
        store = int(input("Car Model (name) : "))

        query1 = "SELECT COUNT(Car_ID) as Number_sold FROM car WHERE car.Car_name='%s'" %(store)
        
        print(query1)
        cur.execute(query1)
        result=cur.fetchone()
        con.commit()
        
        print("Cars with specified details : ", result["Number_sold"])

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        addCustomer()
    elif(ch == 2):
        addCar()
    elif(ch == 3):
        addPincode()
    elif(ch == 4):
        addAward()
    elif(ch == 5):
        addStore()
    elif(ch == 6):
        changeSell()
    elif(ch == 7):
        changeDisplayStore()
    elif(ch == 8):
        deletecustomer()
    elif(ch == 9):
        searchPincode()
    elif(ch == 10):
        carSold()
    elif(ch == 11):
        car()
    else:
        print("Error: Invalid Option")

# Global
while(1):
    tmp = sp.call('clear', shell=True)

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='Pavan@12345',
                              db='dna_project',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                print("1. Add Customer") 
                print("2. Add Car")  
                print("3. Add Areas Served for Store") 
                print("4. Add Award") 
                print("5. Add Store") 
                print("6. Add Seller and Buyer") 
                print("7. Change Display Store") 
                print("8. Delete Customer") 
                print("9. Find Stores Serving a Particular Area")
                print("10. List cars sold in a Store manufactured by a specific Company")
                print("11. Number of cars sold of a model")
                print("12. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 12:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
