from fruit import Fruit
from boat import Boat

#create a boat and some fruit
boat = Boat('Queen Mary', 'London', 'Lisbon')
fruit1 = Fruit('Bananas', 10)
fruit2 = Fruit('Avacado', 10)
fruit3 = Fruit('Oranges', 23)

#append fruit
boat.cargo_list.append(fruit1)
boat.cargo_list.append(fruit2)
boat.cargo_list.append(fruit3)

#alternative option
boat.add_cargo(fruit1)
boat.add_cargo(fruit2)
boat.add_cargo(fruit3)

#printing our lists
print(boat.cargo_list)

boat.print_cargo_list()


# print(boat)
# print(boat.name)
# print(boat.destination)
# print(boat.current_location)
# print(boat.cargo_list)



# bana = Fruit('Bananas', '10')
# print(bana)
# print(bana.kg_of_fruit)
# print(bana.type_of_fruit)
#
# bana.describe()