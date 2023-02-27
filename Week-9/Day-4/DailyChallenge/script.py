
class Person:

    def __init__(self, name, list_love, list_hate):
        self.name = name
        self.list_love = list_love
        self.list_hate = list_hate

    def taste(self, food):
        end_of_str = '!'
        if food in self.list_hate:
            end_of_str = 'and loves it!'
        elif food in self.list_love:
            end_of_str = 'and hates it!'
        return f"{self.name} eats the {food} {end_of_str}"


p1 = Person("Sam", ["ice cream"], ["carrots"])
print(p1.taste("ice cream"))
print(p1.taste("cheese"))
print(p1.taste("carrots"))
