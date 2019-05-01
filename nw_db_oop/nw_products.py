import pyodbc

class NwProducts:
    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.docker_db_instance = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL SERVER}; SERVER='+ self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.docker_db_instance.cursor()

    def __sql_query_no_transaction(self, sql_query):
        return self.cursor.execute(sql_query)

    def print_all_product_records(self):
        #created a query to select all
        #used the cursor to execute this query
        query_records = self.__sql_query_no_transaction("SELECT * FROM Products")
        #Continuosly iterate (while)
            # print out each record (fetchone())
            # We will break when the record is none
        while True:
            record = query_records.fetchone()
            if record is None:
                break
            print(record)

    def print_average_unit_price(self):
        # get the price of the products
        query_records = self.__sql_query_no_transaction("SELECT * FROM Products")
        # store them in a list
            #get each price out and then store in list
        total_unit_price = []
        while True:
            record = query_records.fetchone()
            if record is None:
                break #break when there are no more records
            total_unit_price.append(record.UnitPrice)


        #Total sum of prices/number of units(count)
        print(sum(total_unit_price)/len(total_unit_price))




        # total sum of price / number of units (count)