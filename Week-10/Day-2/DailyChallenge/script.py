from deep_translator import GoogleTranslator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
eng_words = {}

for word in french_words:
    eng_words[word] = GoogleTranslator(source='auto', target='en').translate(word)

print(eng_words)
