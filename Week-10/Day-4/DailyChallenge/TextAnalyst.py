import re

class Text:

    @classmethod
    def create_from_file(cls, path):
        with open(path) as f:
            text = f.read()
        return Text(text)

    def __init__(self, text):
        self.text = text
        self.list_of_words = ' '.join(self.text.split()).split(' ')

    def frequency_of_word(self):
        unique_words = set(self.list_of_words)
        frequency = {}
        for word in unique_words:
            frequency[word] = self.list_of_words.count(word)
        return dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))

    def unique_words(self):
        return list(set(self.list_of_words))

    def most_common_word(self):
        unique_words = set(self.list_of_words)
        frequency = {}
        for word in unique_words:
            frequency[word] = self.list_of_words.count(word)
        return list(dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True)).keys())[0]


class TextModification(Text):
    @classmethod
    def create_from_file(cls, path):
        with open(path) as f:
            text = f.read()
        return TextModification(text)

    def __init__(self, text):
        super().__init__(text)
        f = open('stop_words_english.txt')
        words = f.read()
        self.stop_list = words.split('\n')

    def normalize_text(self):
        return self.remove_stop_list(self.remove_special_char(self.remove_punctuation()))

    def remove_punctuation(self, text=''):
        if text == '':
            text = self.text
        return re.sub(r'[.,"\'-?:!;]', '', text)

    def remove_stop_list(self, text=''):
        if text == '':
            text = self.text
        list_of_words = text.lower().split(' ')
        final_list = [word for word in list_of_words if word not in self.stop_list]
        return ' '.join(final_list)

    def remove_special_char(self, text=''):
        if text == '':
            text = self.text
        return re.sub(r'[^a-zA-Z0-9 ]', ' ', text)
