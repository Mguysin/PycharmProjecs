class Fruit():
    def __init__(self, name='', kg='', grade_quality='', treated=''):
        self.type_of_fruit = name
        self.kg_of_fruit = kg
        grade_quality = grade_quality
        treated = treated

    def describe(self):
        print(f"Carrying {self.type_of_fruit} - around" + str({self.kg_of_fruit}) + "Tones")

    def save(self):
        pass


    def read_all(self):
        query = 'SELECT * FROM Fruits;'
        cursor.execute(query)
        fruit_results = cursor.fetchall()

        print('Fruits on ship and weight in kg')
        for fruit in fruit_results:
            print(f"Fruits: {fruit.type_of_fruit} - weight: {fruit.kg_of_fruit}")
            print(fruit.type_of_fruit, fruit.kg_of_fruit)


    def save(self):
        query = (f"INSERT INTO Fruits(type_of_fruit, kg_of_fruit) VALUES '{self.type_of_fruit}', '{self.kg_of_fruit}'")
        cursor.execute(query)
        docker_Shipping_Cargo.commit()
        print('Executed save fruit')

    def append_to_list(self):
        query = 'SELECT * FROM Fruits'
        cursor.execute(query)
        fruit_results = cursor.fetchall()

        for fruit in fruit_results:
            append_fruit = Fruit(fruit.FruitType, fruit.Weight_in_kg)
            self.fruit_list.append(append_fruit)
        print(self.fruit_list)


    # def read_all(self):
    #     # created a query to select all
    #     # used the cursor to execute this query
    #     query_records = self.__sql_query_no_transaction("SELECT * FROM Fruits")
    #     # Continuosly iterate (while)
    #     # print out each record (fetchone())
    #     # We will break when the record is none
    #     while True:
    #         record = query_records.fetchone()
    #         if record is None:
    #             break
    #         print(record)


    # def save(self):
    #     name = input('Enter type of fruit')
    #     kg = input('Enter weight (kg)')
    #     grade_quality = input('Enter grade')
    #     treated = input('Clarify if treated')
    #
    #     fruit_object = Fruit(name, kg, grade_quality, treated)







    # def load_fruits(self):
    #     fruits = self.sql_query_no_transaction("SELECT * FROM Fruits")
    #     while True:
    #         fruit_objects = fruits.fetchone()
    #         if fruit_objects is None:
    #             break
    #             print(fruit_objects)
