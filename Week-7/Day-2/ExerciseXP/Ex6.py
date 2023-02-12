
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


def show_magicians():
    for magician in magician_names:
        print(magician)


def make_great():
    for x in range(0, len(magician_names)):
        magician_names[x] += ' the Great'


make_great()
show_magicians()