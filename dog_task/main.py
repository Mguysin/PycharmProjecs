from animal import *
from dog import *
from dog_lesson import *

class Main(Animal, Dog, Dog_lesson):
    def __init__(self, main):
        super()._init_(name)
        self.main=main
while True:
    print('Please make a selection')
    selection=int(input('Select 1 to add a new dog, select 2 to view the list of dog lessons, select 3 to add a dog to a lesson'))

    if selection == 1:
        print('Adding a new dog:')
        name=input('Enter the dog name')
        id=input('Enter the dog id')
        age=input('Enter the dog age')
        new_dog=Dog(name, id, age)
