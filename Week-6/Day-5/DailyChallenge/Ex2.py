items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = int(input('Enter amount in your wallet: '))
can_afford = []

for key, value in items_purchase.items():
    int_value = int(value.replace('$', ''))
    if int_value <= wallet:
        can_afford.append(key)

can_afford.sort()
if len(can_afford) > 0:
    print(can_afford)
else:
    print('Nothing')