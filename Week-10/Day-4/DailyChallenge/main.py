import TextAnalyst

text_1 = TextAnalyst.Text('A good book would sometimes cost as much as a good house.')
print(text_1.frequency_of_word())
print(text_1.unique_words())
print(text_1.most_common_word())


text_modificator = TextAnalyst.TextModification.create_from_file('the_stranger.txt')
text_2 = TextAnalyst.Text(text_modificator.normalize_text())
print(text_2.frequency_of_word())
print(text_2.unique_words())
print(text_2.most_common_word())
