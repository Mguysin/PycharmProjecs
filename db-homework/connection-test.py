import pyodbc
#Our variables to create a connection
connection = 'Microsoft SQL Server'
server = 'localhost,1433'
database = 'ShopDatabase'
username = 'SA'
password = 'Passw0rd2018'

#Making a connection
docker_ShopDatabase = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL SERVER}; SERVER='+ server+';DATABASE='+database+';UID='+username+';PWD='+password)

#Creating a cursor that can execute SQL functions on connected db
cursor = docker_ShopDatabase.cursor()


#Executing the SQL
cursor.execute("SELECT * FROM Persons")





#Getting the wors out of the results of the execution
rows = cursor.fetchall()
description = cursor.description

cursor.execute()

print(cursor.description)

print(len(rows))
print(type(rows))

for row in rows:
    print(type(row))
    print(row.LastName)


cursor = docker_ShopDatabase.cursor()

def LastName(LastName):
    query = f"SELECT FROM Persons WHERE LastName = '{LastName}'"
    rows= cursor.execute(query)
    return rows.fetchall()

sql = LastName('Smith')
print(sql)
for data in sql:
    print(data.LastName)





# def add_persons():
#     query = "INSERT INTO Persons(LastName, FirstName, Address, CIty) VALUES('Smith', 'Michael','North London', 'London');"
#     row = cursor.execute(query)
#     return row.fetchall()
#
# add_persons()
#
# #Getting the wors out of the results of the execution
# rows = cursor.fetchall()
# description = cursor.description
#

# print(cursor.description)



# print(len(rows))
# print(type(rows))
#
# for row in rows:
#     print(type(row))
#     print(row.ContactName)
#     print(row.Fax)
#     print(row.Phone)
