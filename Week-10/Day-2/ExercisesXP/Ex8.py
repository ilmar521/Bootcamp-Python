from faker import Faker
fake = Faker()

users = []
for i in range(5):
    users.append(
        {'name': fake.name(),
         'adress': fake.address(),
         'language_code': fake.language_code()})
print(users)
