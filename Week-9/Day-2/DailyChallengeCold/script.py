list_of_strings = ['Tom,19,80', 'John,20,90', 'Jony,17,93', 'Jony,17,91', 'Json,21,85']

list_of_tupples = []
for string in list_of_strings:
    list_of_tupples.append(tuple(string.split(',')))

list_of_tupples.sort(key=lambda x: (x[0], x[1], x[2]))
print(list_of_tupples)