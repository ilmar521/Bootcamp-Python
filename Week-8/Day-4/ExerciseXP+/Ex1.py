
class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        self.members.append(kwargs)

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return True if member['age'] > 18 else False
        return False

    def family_presentation(self):
        list_names = []
        for member in self.members:
            list_names.append(member['name'])
        print(f'{self.last_name} - {", ".join(list_names)}')


family = Family([{'name':'Michael','age':35,'gender':'Male','is_child':False},{'name':'Sarah','age':32,'gender':'Female','is_child':False}], 'Smith')
family.born(name='Jack', age=14, gender='Male', is_child=True)
print(family.is_18('Michael'))
family.family_presentation()