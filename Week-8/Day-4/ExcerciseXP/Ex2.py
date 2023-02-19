
class Dog:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f'{self.name} is barking')

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        print(f'{self.name if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight else other_dog.name} is winner between {self.name} and {other_dog.name}')


dog1 = Dog('Bob', 12, 40)
dog2 = Dog('Jack', 10, 50)
dog3 = Dog('Puppy', 8, 60)

dog1.fight(dog2)
dog1.fight(dog3)
dog2.fight(dog3)
