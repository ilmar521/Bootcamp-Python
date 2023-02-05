user_height = input('Enter your height in inches: ')

if int(user_height) * 2.54 > 145:
    print('Congrats! You are tall enough to ride!')
else:
    print('Sorry, but you don\'t tall enough to ride. You should just grow a little bit more.')