
class Door:
    objs = 0
    KEYS = 1

    @staticmethod
    def recursion_find_way(door_from, door_to, solve):
        if door_to in door_from.next:
            if door_to.locked:
                if Door.KEYS == 0:
                    return solve
                Door.KEYS -= 1
            solve['can_go'] = True
            solve['way_to_door'] = f"{door_from.name} -- {door_to.name}"
            return solve

        for door in door_from.next:
            if door.locked:
                if Door.KEYS == 0:
                    return solve
                Door.KEYS -= 1
            Door.recursion_find_way(door, door_to, solve)
            if solve['can_go']:
                solve['way_to_door'] = f"{door_from.name} -- " + solve['way_to_door']
                return solve

    def __init__(self, name, locked, next):
        self.id = Door.objs
        self.name = name
        self.locked = locked
        self.next = next
        Door.objs += 1

    def can_go_to(self, other_door):
        solve = {'way_to_door': '', 'can_go': False}
        Door.recursion_find_way(self, other_door, solve)
        return solve


d_4_1 = Door('d_4_1', False, [])
d_3_2 = Door('d_3_2', True, [d_4_1])
d_3_1 = Door('d_3_1', False, [])
d_2_2 = Door('d_2_2', False, [d_3_1, d_3_2])
d_2_1 = Door('d_2_1', False, [])
d_1_1 = Door('d_1_1', False, [d_2_1, d_2_2])

print(d_1_1.can_go_to(d_4_1))

