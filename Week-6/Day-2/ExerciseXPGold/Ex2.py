month = input('Enter ')
month = int(month)

if month == 12 or month == 1 or month == 2:
    print('Now is winter')
elif 3 <= month <= 5:
    print('Now is spring')
elif 6 <= month <= 8:
    print('Now is summer')
elif 7 <= month <= 11:
    print('Now is autumn')
else:
    print('I don\'t know this part of year')