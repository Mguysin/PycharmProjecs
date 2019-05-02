import pyodbc

#Our variable to create a connection

server = 'localhost,1433'

database = 'Northwind'

username = 'SA'

password = 'Passw0rd2018'



#Making a connection

docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)



#Creating a cursor that can execute SQL funtions on connected db

cursor = docker_Northwind.cursor()



# Executing the SQL

cursor.execute("SELECT * FROM Customers WHERE Fax IS NULL")



#Getting the rows out of the results of the execution

rows = cursor.fetchall()

description = cursor.description





print(len(rows))

print(type(rows))



for row in rows:

    print(type(row))

    print(row.ContactName)

    print(row.Fax)

    print(row.Phone)