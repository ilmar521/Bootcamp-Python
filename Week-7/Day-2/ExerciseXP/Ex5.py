
def make_shirt(text, size='large'):
    if size == 'large' or size == 'medium':
        text = 'I love Python'
    else:
        text = 'I love Python and JS'
    print(f'The size of the shirt is {size} and the text is {text}')


make_shirt(size='medium', text='any text')
