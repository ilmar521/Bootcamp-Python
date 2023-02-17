class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


Cats = [Cat('Bob', 5), Cat('Jack', 8), Cat('Muur', 7)]


def oldest_cat():
    old_cat = Cats[0]
    for each_cat in Cats:
        if each_cat.age > old_cat.age:
            old_cat = each_cat

    print(f'The oldest cat is {old_cat.name}, and is {old_cat.age} years old.')


oldest_cat()
