
import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase + string.ascii_uppercase
    rand_string = ''.join([random.choice(letters) for i in range(length)])
    print("Secret key", rand_string)


generate_random_string(256)
