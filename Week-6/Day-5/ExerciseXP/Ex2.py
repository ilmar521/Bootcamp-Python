
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0
for value in family.values():
    if 12 >= value >= 3:
        total_cost += 10
    elif value > 12:
        total_cost += 15

print(total_cost)