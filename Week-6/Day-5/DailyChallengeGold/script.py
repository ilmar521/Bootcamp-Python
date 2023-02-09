text = input('Enter a text: ')
way = input('Enter what action you want to do with text (encryption/decryption): ')
step = int(input('Enter step of cypher: '))

out_text = ''
for letter in text:
    if letter.isalpha():
        if way == 'encryption':
            out_text += chr(ord(letter) + step)
        else:
            out_text += chr(ord(letter) - step)
    else:
        out_text += letter

print(out_text)