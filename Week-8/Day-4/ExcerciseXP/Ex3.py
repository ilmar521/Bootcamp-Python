from Ex2 import Dog
from random import randint


class PetDog(Dog):

    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        self.bark()
        self.trained = True

    def play(self, *dogs):
        dogs_list = [self.name]
        for dog in dogs:
            dogs_list.append(dog.name)
        print(f'{", ".join(dogs_list)} all play together')

    def do_a_trick(self):
        list_actions = ['does a barrel roll', 'stands on his back legs', 'shakes your hand', 'plays dead']
        if self.trained:
            print(f'{self.name} {list_actions[randint(0,3)]}')


pet_dog1 = Dog('Bob', 12, 40)
pet_dog2 = Dog('Jack', 10, 50)
pet_dog3 = PetDog('Carl', 11, 35)
pet_dog3.train()
pet_dog3.play(pet_dog1, pet_dog2)
pet_dog3.do_a_trick()
