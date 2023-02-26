
class Character:

    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    def basic_attack(self, Other):
        if isinstance(Other, Character):
            Other.life -= self.attack

    def __repr__(self):
        return f"{self.name}: life - {self.life}, attack - {self.attack}"


class Druid(Character):

    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"I'm {name} the trees call me!")

    def meditate(self):
        self.life += 10
        self.attack -= 2

    def animal_help(self):
        self.attack += 5

    def fight(self, Other):
        if isinstance(Other, Character):
            Other.life -= (0.75 * self.life + 0.75 * self.attack)


class Warrior(Character):

    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"I'm {name} and I swallow blood of my enemies!")

    def brawl(self, Other):
        if isinstance(Other, Character):
            Other.life -= 2 * self.attack
            self.life += 0.5 * self.attack

    def train(self):
        self.attack += 2

    def roar(self, Other):
        if isinstance(Other, Character):
            Other.attack -= 3


class Mage(Character):

    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"I'm {name}, my magic is genuine power!")

    def curse(self, Other):
        if isinstance(Other, Character):
            Other.attack -= 2

    def summon(self):
        self.attack += 3

    def cast_spell(self, Other):
        if isinstance(Other, Character):
            Other.life -= self.attack / self.life