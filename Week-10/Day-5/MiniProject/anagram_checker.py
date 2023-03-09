import requests
import itertools


class AnagramChecker:

    @classmethod
    def create_instance(cls):
        response = requests.get("http://norvig.com/ngrams/sowpods.txt")
        if response.status_code != 200:
            raise f'norvig.com return status code {response.status_code}!'
        list_of_words = response.text.split('\n')
        return AnagramChecker(list_of_words)

    def __init__(self, list_of_words):
        self.list_of_words = list_of_words

    def is_valid_word(self, word):
        return word.upper() in self.list_of_words

    def get_anagrams(self, analize_word):
        all_annagrams = set(["".join(perm) for perm in itertools.permutations(analize_word)])
        list_of_annagrams = [word for word in all_annagrams if word.upper() in self.list_of_words and word.upper() != analize_word.upper()]
        return list_of_annagrams
# missing is_anagram function

ins = AnagramChecker.create_instance()
