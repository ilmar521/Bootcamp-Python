sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []

for x in sandwich_orders:
    finished_sandwiches.append(x)
sandwich_orders.clear()

for x in finished_sandwiches:
    print(f'I made your {x}')