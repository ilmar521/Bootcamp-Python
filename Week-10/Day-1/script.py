import os

for i in range(16, 17):
    os.mkdir(f'../../Week-{i}')
    os.chdir(f'../../Week-{i}')
    for n in range(1, 6):
        os.mkdir(f'./Day-{n}')
        os.chdir(f'./Day-{n}')
        if n == 2 or n == 4 or n ==5:
            os.mkdir(f'./DailyChallenge')
            os.mkdir(f'./ExerciseXP')
        os.chdir('../')
    os.chdir('../')

