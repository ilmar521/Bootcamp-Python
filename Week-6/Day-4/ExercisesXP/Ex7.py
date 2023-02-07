str_fav_fruits = input('Enter your favorite fruits (please separate fruits by space): ')
fav_fruits = str_fav_fruits.split(' ')

fruit = input('Enter a fruit: ')

if fruit in fav_fruits:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy')