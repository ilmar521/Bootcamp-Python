

def calculate(x):
    list_numbers = [x * i for i in range(1, 5)]
    print(sum(list(map(int, list_numbers))))


x = input('Enter a number: ')
if len(x) == 1 and x.isdigit():
    calculate(x)
else:
    print('You enter invalid number!')
