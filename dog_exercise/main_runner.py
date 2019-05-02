from animal import*
from dog import*
from dog_lesson import*

list_all_lessons = []

lesson_1.append_dog(group_1)
lesson_2.append_dog(group_2)
lesson_3.append_dog(group_3)

list_all_lessons.append(lesson_1)
list_all_lessons.append(lesson_2)
list_all_lessons.append(lesson_3)



# for lesson in list_all_lessons:
#     if lesson.location == 'Putney':
#         lesson.dog_list.append(group_1)
#     elif lesson.location == 'Wimbledon':
#         lesson.dog_list.append(group_2)
#     elif lesson.location == 'Clapham':
#         lesson.dog_list.append(group_3)



#
# for lesson in list_all_lessons:
#     if lesson.location == 'Putney':




# print(lesson_1.location, lesson_1.dog_list)


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
        print('You chose to view the list of dog lessons')
        for lesson in list_all_lessons:
            print(lesson.location, lesson.dog_list, lesson.time)


    if selection ==3:
        print('You chose to add your dog to a lesson')
        print('Please enter the details of your dog below:')
        name = input('Enter the dog name')
        id = input('Enter the dog id')
        age = input('Enter the dog age')
        added_dog = Dog(name, id, age)

        for lesson in list_all_lessons:
            print(lesson.location, lesson.dog_list, lesson.time)


        choice = int(input('Select lesson(1-3) that you want to add your dog to'));
        if choice == 1:
            group_1.append(added_dog.name)
            print('Your lesson location is', lesson_1.location, 'The list of dogs is', lesson_1.dog_list, 'The time of the lesson is', lesson_1.time)
        if choice == 2:
            group_2.append(added_dog.name)
            print('Your lesson location is', lesson_2.location, 'The list of dogs is', lesson_2.dog_list, 'The time of the lesson is', lesson_2.time)
        if choice == 3:
            group_3.append(added_dog.name)
            print('Your lesson location is', lesson_3.location, 'The list of dogs is', lesson_3.dog_list, 'The time of the lesson is', lesson_3.time)


            # lesson_1.append(added_dog);
            # print('Your lesson location is', lesson_1.location, 'List of pariticipating dogs is', lesson_1.dog_list);
        # elif choice == 2:
        #     print('Your lesson location is', lesson_2.location,'List of participating dogs is', lesson_2.dog_list);
        # elif choice == 3:
        #     print('Your lesson location is', lesson_3.location, 'List of participating dogs is', lesson_3.dog_list);
