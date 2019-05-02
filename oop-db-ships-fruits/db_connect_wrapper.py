import pyodbc

#Our variable to create a connection

server = 'localhost,1433'
database = 'fruits_and_ships'
username = 'SA'
password = 'Passw0rd2018'



#Making a connection
docker_fruits_and_ships = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

#Creating a cursor that can execute SQL funtions on connected db
cursor = docker_fruits_and_ships.cursor()

# Executing the SQL
cursor.execute("SELECT * FROM Fruits")



#Getting the rows out of the results of the execution

rows = cursor.fetchall()

description = cursor.description





# print(len(rows))
#
# print(type(rows))



for row in rows:

    # print(type(row))

    print(row.type_of_fruit)

    print(row.kg_of_fruit)

    print(row.grade_quality)

    print(row.treated)














