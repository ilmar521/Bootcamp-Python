
from Ex1 import Family


class TheIncredibles(Family):
    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] > 18:
                    print(member['power'])
                else:
                    raise Exception(f"{name} are not over 18 years old.")

    def incredible_presentation(self):
        super().family_presentation()
        list_powers = []
        for member in self.members:
            list_powers.append(f'{member["incredible_name"]} - {member["power"]}')
        print(f'{", ".join(list_powers)}')


incredibles = TheIncredibles([{'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
                              {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}], 'Smith')
incredibles.use_power('Michael')
incredibles.incredible_presentation()
incredibles.born(name='Jack', age=3, gender='Male', is_child=True, power='Unknown Power', incredible_name='Baby Jack')
incredibles.incredible_presentation()
