from random import shuffle

user_string = input('Please enter a string: ')

if len(user_string) > 10:
    print('string too long')
elif len(user_string) < 10:
    print('string not long enough')

print(user_string[0] + user_string[len(user_string) - 1])

new_str = ''
for x in user_string:
   new_str += x
   print(new_str)

user_string_arr = list(user_string);
shuffle(user_string_arr)

print(''.join(user_string_arr))