
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")


davids_dog = Dog('Rex', 50)
print(f"Name David's dog is {davids_dog.name} and its height is {davids_dog.height}")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup', 20)
print(f"Name Sarah's dog is {sarahs_dog.name} and its height is {sarahs_dog.height}")
sarahs_dog.bark()
sarahs_dog.jump()


if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is a bigger than {sarahs_dog.name}")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is a bigger than {davids_dog.name}")
else:
    print(f"{sarahs_dog.name} and {davids_dog.name} have the same height")
