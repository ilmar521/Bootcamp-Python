sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []

print('Sorry, we don\'t have any pastrami!')
while sandwich_orders.count('Pastrami sandwich') > 0:
    index = sandwich_orders.index("Pastrami sandwich")
    sandwich_orders.pop(index)

for x in sandwich_orders:
    finished_sandwiches.append(x)
sandwich_orders.clear()

for x in finished_sandwiches:
    print(f'I made your {x}')