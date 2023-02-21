
class Door:
    def __init__(self):
        self.is_opened = False

    def open_door(self):
        self.is_opened = True

    def close_door(self):
        self.is_opened = False


class BlockedDoor(Door):
    def open_door(self):
        raise Exception('Blocked door cannot be opened or closed')

    def close_door(self):
        raise Exception('Blocked door cannot be opened or closed')


door = BlockedDoor()
door.open_door()
