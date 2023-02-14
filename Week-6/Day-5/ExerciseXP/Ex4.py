users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

disney_users_A = {}
for i, item in enumerate(users):
    disney_users_A[item] = i

print(disney_users_A)

disney_users_B = {}
for i, item in enumerate(users):
    disney_users_B[i] = item

print(disney_users_B)

users.sort()
disney_users_C = {}
for i, item in enumerate(users):
    disney_users_C[item] = i

print(disney_users_C)


disney_users_D = {}
i = 0
for item in users:
    if item[0] == 'M' or item[0] == 'P' or 'i' in item:
        disney_users_D[item] = i
        i += 1
    else:  # it's redundant, there is no need for this else
        continue 

print(disney_users_D)
