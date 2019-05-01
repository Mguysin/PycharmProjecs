from animal import*
from dog import*
from dog_lesson import*

class Main(Dog, Dog_lesson):
    def __init__(self, main):
        super()._init_(name='')
        self.main=main


list_of_lessons=[]
list_of_lessons.append(lesson_1)
list_of_lessons.append(lesson_2)
list_of_lessons.append(lesson_3)



for lesson in (list_of_lessons):
    print(lesson.location, lesson.dog_list.append(group_1))


while True:
    print('Please make a selection')
    selection = int(input('Select 1 to add a new dog, select 2 to view the list of dog lessons, select 3 to add a dog to a lesson'))

    if selection == 1:
        print('Adding a new dog:')
        name = input('Enter the dog name')
        id = input('Enter the dog id')
        age = input('Enter the dog age')
        new_dog = Dog(name, id, age)
        list_of_dogs.append(new_dog)
        print('New dog has now been added to the list')
        for dogs in list_of_dogs:
            print(dogs.name)

    if selection == 2:
        print('You selected the option to view the available dog lessons')
        for lesson in list_location:
            print(lesson.location,)
        choice = int(input('Select the the location (1-3) of a dog lesson'))
        if choice == 1:
            print('You selected', list_location[0].location)
            print('See the list of dogs for this lesson below:')
            for list in group_1:
                print(list.name)
        if choice == 2:
            print('You selected', list_location[1].location)
            print('See the list of dogs for this lesson below:')
            for list in group_2:
                print(list.name)
        if choice == 3:
            print('You selected', list_location[2].location)
            print('See the list of dogs for this lesson below:')
            for list in group_3:
                print(list.name)

    if selection == 3:
        print('Enter details of the dog')
        name = input('Enter the dog name')
        id = input('Enter the dog id')
        age = input('Enter the dog age')
        added_dog = Dog(name, id, age)

        for lesson in list_location:
            print(lesson.location)
        option = int(input('Select the class from above(1-3)'))

        if option == 1:
            print('Adding your dog to', list_location[0])
            print('See the list of dogs below:')
            group_1.append(added_dog)
            for dog in group_1:
                print(dog.name)
        if option == 2:
            print('Adding your dog to', list_location[1])
            print('See the list of dogs below:')
            group_2.append(added_dog)
            for dog in group_2:
                print(dog.name)
        if option == 3:
            print('Adding your dog to', list_location[2])
            print('See the list of dogs below:')
            group_3.append(added_dog)
            for dog in group_3:
                print(dog.name)





