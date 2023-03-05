import os

for i in range(1, 6):
    os.mkdir(f'./Week-{i}')
    os.chdir(f'./Week-{i}')
    for n in range(1, 6):
        os.mkdir(f'./Day-{n}')
        os.chdir(f'./Day-{n}')
        os.mkdir(f'./lesson')
        os.mkdir(f'./homework')
        os.chdir('../')
    os.chdir('../')

