from animal import*


class Dog_lesson(Animal):

    def __init__(self, location, dog_list = [], time=''):
        super()._init_(name='')
        self.location=location
        self.dog_list= dog_list
        self.time = time

    def append_dog(self, dog):
        self.dog_list.append(dog)
        #write this method



lesson_1 = Dog_lesson('Putney', [], '2 pm')
lesson_2 = Dog_lesson('Wimbledon', [], '3 pm')
lesson_3 = Dog_lesson('Clapham', [], '4 pm')




# for lessons in list_location:
#     print(lessons.location, lessons.dog_list)


#
#
# list_of_dog_lessons=[]
#
# dog_lesson_1 = Dog_lesson('Putney', 'list')
# dog_lesson_2 = Dog_lesson('Wimbledon', 'list')
# dog_lesson_3 = Dog_lesson('Clapham', 'list')
#
#
# # dog_list_1 = [dog_1.name,dog_3.name, dog_4.name]
# # dog_list_2= [dog_3.name, dog_5.name]
# # dog_list_3= [dog_1.name, dog_5.name]
#
#
# list_of_dog_lessons.append(dog_lesson_1)
# list_of_dog_lessons.append(dog_lesson_2)
# list_of_dog_lessons.append(dog_lesson_3)
# #
# # print(list_of_dog_lessons)
# #
# #
# # print('hello')