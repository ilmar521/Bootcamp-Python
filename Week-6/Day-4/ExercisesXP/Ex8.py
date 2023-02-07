list_toppings = []

while True:
    topping = input('Enter a topping: ')
    if topping == 'quit':
        break
    else:
        list_toppings.append(topping)
        print('Great! We\'ll add this one to your pizza!')

print('All your toppings ' + ' '.join(list_toppings) + f'. Total price: {10 + len(list_toppings) * 2.5}')