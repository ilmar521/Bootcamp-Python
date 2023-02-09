your_number = int(input('Enter a number for checking: '))

list_dividers = []
for x in range(1, your_number):
    if your_number % x == 0:
        list_dividers.append(x)

print(sum(list_dividers) == your_number)