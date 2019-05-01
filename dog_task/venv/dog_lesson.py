from animal import*
from dog import*

class Dog_lesson():
    def __init__(self, location, dog_list):
        super()._init_()
        self.location=location
        self.dog_list=dog_list

list_of_dog_lessons=[]

dog_lesson_1 = Dog_lesson('Putney', 'list')
dog_lesson_2 = Dog_lesson('Wimbledon', 'list')
dog_lesson_3 = Dog_lesson('Clapham', 'list')


dog_list_1 = [dog_1.name,dog_3.name, dog_4.name]
dog_list_2= [dog_3.name, dog_5.name]
dog_list_3= [dog_1.name, dog_5.name]


list_of_dog_lessons.append(dog_lesson_1)
list_of_dog_lessons.append(dog_lesson_2)
list_of_dog_lessons.append(dog_lesson_3)

print(list_of_dog_lessons)


