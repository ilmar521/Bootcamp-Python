word = input('Enter a word: ')
dict1 = {}

uniq_let = []
for letter in word:
    if letter not in uniq_let:
        uniq_let.append(letter)

for letter in uniq_let:
    dict1[letter] = []
    for i, letter2 in enumerate(word):
        if letter == letter2:
            dict1[letter].append(i)

print(dict1)