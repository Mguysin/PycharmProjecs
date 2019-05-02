from animal import *
from dog_lesson import *

class Dog(Animal):

    def __init__(self, name, id, age):
        super()._init_(name)
        self.name=name
        self.id=id
        self.age=age


list_of_dogs=[]

dog_1 = Dog('Teddy', 'b134', '5')
dog_2 = Dog('Rex', 'b127', '3')
dog_3 = Dog('Mike', 'b179', 2)
dog_4 = Dog('John', 'b179', '4')
dog_5 = Dog ('Matt', 'b149', '3')

list_of_dogs.append(dog_1)
list_of_dogs.append(dog_2)
list_of_dogs.append(dog_3)
list_of_dogs.append(dog_4)
list_of_dogs.append(dog_5)


dog_groups=[]

group_1 = [dog_1.name, dog_3.name, dog_5.name]
group_2 = [dog_2.name, dog_4.name, dog_5.name]
group_3 = [dog_2.name, dog_3.name, dog_4.name]



# dog_groups.append(group_1)
# dog_groups.append(group_2)
# dog_groups.append(group_3)
#






# while True:
#     print('Please make a selection')
#     selection = int(
#         input('Select 1 to add a new dog, select 2 to view the list of dog lessons, select 3 to add a dog to a lesson'))
#
#     if selection == 1:
#         print('Adding a new dog:')
#         name = input('Enter the dog name')
#         id = input('Enter the dog id')
#         age = input('Enter the dog age')
#         new_dog = Dog(name, id, age)
#         list_of_dogs.append(new_dog)
#         print('New dog has now been added to the list')
#         for dogs in list_of_dogs:
#             print(dogs.name, dogs.id, dogs.age)
#
#     if selection == 2:
#         print('You selected the option to view the available dog lessons')
#         print('The list of dog lessons is the following:')
#         print(list_111)
#
