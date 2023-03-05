import string
import random

final_str = []
for i in range(5):
    final_str.append(random.choice(string.ascii_uppercase) if i % 2 == 0 else random.choice(string.ascii_lowercase))
print(''.join(final_str))
