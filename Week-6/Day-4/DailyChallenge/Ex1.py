
number = int(input('Enter a number: '))
length = int(input('Enter a length: '))

output_list = []

if length > 0:
    for x in range(1, length):
        output_list.append(number * x)
    print(output_list)
else:
    print('Please enter length more than 0 value')