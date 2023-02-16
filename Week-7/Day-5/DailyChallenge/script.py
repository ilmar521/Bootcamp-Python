
inp_str = input("Enter a string: ")
list_str = [str for str in inp_str.split(',')]
list_str.sort()
print(','.join(list_str))