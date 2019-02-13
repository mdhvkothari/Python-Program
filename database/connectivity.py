import mysql.connector
from mysql.connector import Error


try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "test"   
    )

    #make a cursor 

    mycursor = mydb.cursor()
    firstname = input()
    lastname = input()
    
    sql_insert_query = """INSERT INTO `data`(`firstname`, `lastname`) VALUES (%s,%s)"""

    insert_tuple = (firstname,lastname)
    
    mycursor.execute(sql_insert_query,insert_tuple)
    mydb.commit()
    print("Sucesssful inserted")
    
    #mycursor.execute("SHOW DATABASES")
    #for i in mycursor:
    #    print(i)

    mycursor.execute("SELECT firstname FROM data")
    #.fetchone() will return first row in of the table
    myresult = mycursor.fetchall()
    
    for j in myresult:
        print(j)
    
    a="madhav"
    row=0
    for i in myresult:
        result = myresult[row][0]
        if result == a:
            print("yes")
        row+=1

    
except Error as e:
    mydb.rollback()
    print(e)
    
    
    
    
    
