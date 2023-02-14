
character = input('Enter a char: ')
string = input('Enter a string: ')

list_char = [char for char in string if char == character]
print(len(list_char))