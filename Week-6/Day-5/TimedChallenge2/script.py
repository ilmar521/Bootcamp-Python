sentence = input('Enter a sentence: ')
sentence_arr = sentence.split(' ')

for x in range(len(sentence_arr) - 1, -1, -1):
    print(sentence_arr[x], end=' ')
