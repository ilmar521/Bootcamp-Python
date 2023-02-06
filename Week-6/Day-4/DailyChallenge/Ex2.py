
input_string = input('Enter a word: ')
input_string_arr = list(input_string)
input_string_arr2 = []
for element in input_string_arr:
    if element not in input_string_arr2:
        input_string_arr2.append(element)

print("".join(input_string_arr2))
