str_family_ages = input('Enter your ages separated by space: ')
family_ages = str_family_ages.split(' ')
total_cost = 0
for x in family_ages:
    if 12 >= int(x) >= 3:
        total_cost += 10
    elif int(x) > 12:
        total_cost += 15

print(f'Total cost: {total_cost}')

list_teens = ['Mike', 'Bob', 'Peter']

for x in reversed(range(len(list_teens))):
    age = int(input(f'{list_teens[x]} enter your age: '))
    if 16 >= age <= 21:
        list_teens.remove(list_teens[x])

print(list_teens)